import base64
import io
from datetime import datetime
import json
import random
from minio import Minio
from fastapi import FastAPI, BackgroundTasks, Request, HTTPException
from starlette.responses import Response
from pyredis import Client
from Server.util import datetostr_yyyymmddhhmiss, strtodate_yyyymmddhhmmss, to_date_path


minio_service = [
    "192.168.100.21:9000",
    "192.168.100.22:9000"
]

minio_access = "lpr_access"

minio_secret = "lpr_secret"

lpr_buckets = "lprdata"

redis_service = [
    {"host": "192.168.100.20", "port": 6379},
    {"host": "192.168.100.20", "port": 6379},
    {"host": "192.168.100.20", "port": 6379},
]

lpr_error_log = "/Users/zhengguozhen/Downloads/lowi_dev/logs/"

minio_client = Minio(
    minio_service[random.randint(0, len(minio_service) - 1)],
    access_key=minio_access,
    secret_key=minio_secret,
    secure=False
)


def minio_write_image(filename, content):
    my_content = bytes(content, 'utf-8')
    minio_client.put_object(lpr_buckets, filename, io.BytesIO(my_content), length=len(my_content),
                            content_type="application/csv")


def minio_read_image(filename):
    response = None
    try:
        response = minio_client.get_object(lpr_buckets, filename)
        content = response.read()
    finally:
        if response:
            response.close()
            response.release_conn()
    return content


app = FastAPI()


def error_log_txt(ss):
    with open(lpr_error_log+"txt_"+datetostr_yyyymmddhhmiss(datetime.now()), 'a+') as f:
        for s in ss:
            f.write(s["value"]+"\n")


def error_log_jpg(ss):
    with open(lpr_error_log+"jpg_"+datetostr_yyyymmddhhmiss(datetime.now()), 'a+') as f:
        for s in ss:
            f.write(s["key"]+"|"+s["value"]+"\n")


def lpr_process(doc):
    # log
    # prevent redis error
    try:
        redis_config = redis_service[random.randint(0, len(redis_service)-1)]
        redis_client = Client(
            host=redis_config["host"], port=redis_config["port"], encoding="UTF-8")
        for txt in doc["log_data"]:
            # prevent redis set error
            try:
                redis_client.set(txt["key"], txt["value"])
            except Exception as err:
                print(str(err))
                error_log_txt([txt])
        redis_client.close()
    except Exception as err:
        print(str(err))
        error_log_txt(doc["log_data"])
    # jpg
    # prevent minio error
    try:
        for jpg in doc["jpg_data"]:
            filename = jpg["key"]
            path = to_date_path(strtodate_yyyymmddhhmmss(jpg["key"][18:32]))
            # prevent minio write error
            try:
                minio_write_image(path+filename, jpg["value"])
            except Exception as err:
                print(str(err))
                error_log_jpg([jpg])
    except Exception as err:
        print(str(err))
        error_log_jpg(doc["jpg_data"])


@app.get("/")
async def root():
    return {"message": "Hello LPR Server"}


@app.post("/lpr_receive")
async def lpr_receive(request: Request, background_tasks: BackgroundTasks):
    try:
        doc = json.loads(await request.json())
        background_tasks.add_task(lpr_process, doc)
        return {"status": "success"}
    except Exception as err:
        return {"status": "fail " + str(err)}


@app.get("/lpr_img", response_class=Response)
def lpr_img(filename):
    try:
        jpg_data = minio_read_image(filename)
        jpg = base64.b64decode(jpg_data)
        return Response(content=jpg, media_type="image/jpeg")
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail=str(err))
