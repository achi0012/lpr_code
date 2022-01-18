import base64
import datetime
import glob
import json
import os
import random
import uuid

import requests

from Edge import lpr_edge_data_path, lpr_server


def lpr_edge_process():
    filenames = []
    txt_contents = []
    jpg_contents = []
    try:
        # process log file
        for filename in glob.iglob(lpr_edge_data_path + '**/*.txt', recursive=True):
            filenames.append(filename)
            with open(filename, 'r') as txt:
                txt_contents.append(
                    {"key": filename[filename.rfind("/")+1:-4], "value": txt.read()})
        # process img file
        for filename in glob.iglob(lpr_edge_data_path + '**/*.jpg', recursive=True):
            filenames.append(filename)
            with open(filename, 'rb') as img:
                jpg_contents.append(
                    {"key": filename[filename.rfind("/")+1:-4], "value": str(base64.b64encode(img.read()).decode("utf-8"))})
        doc = {"key": str(uuid.uuid1()) + "_" +
               str(int(datetime.datetime.now().timestamp()))}
        doc.update({"log_data": txt_contents})
        doc.update({"jpg_data": jpg_contents})
        resp = requests.post(lpr_server[random.randint(
            0, len(lpr_server) - 1)], json=json.dumps(doc))
        if resp.status_code == 200:
            doc = json.loads(resp.content)
            if doc["status"] == "success":
                print("Post:"+str(len(txt_contents)) +
                      " logs, "+str(len(jpg_contents))+" jpgs")
                print("OK")
                # clear files
                # for f in filenames:
                #     os.remove(f)
        else:
            print("Send Data Error")
    except Exception as err:
        print("Error " + str(err))


if __name__ == "__main__":
    while True:
        try:
            lpr_edge_process()
        except Exception as err:
            print(err)
