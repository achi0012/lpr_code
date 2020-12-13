import base64
import os
from confluent_kafka import Consumer
import vertica_python
from lpr_common import v_conn_info, k_conf_info, topic_img, topic_txt, lpr_server_data_path, target_table


def lpr_consumer_txt():
    txt_value_list = []
    consumer = Consumer(k_conf_info)
    try:
        consumer.subscribe([topic_txt])
        running = True
        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                running = False
            else:
                txt_value_list.append(msg.value().decode("utf-8"))
        with vertica_python.connect(**v_conn_info) as conn:
            with conn.cursor() as cur:
                cur.copy(
                    "Copy " + target_table +
                    " (cctv_id, car_id, record_timestamp, v_type) "
                    "From stdin Delimiter ',' Direct No Commit", "\n".join(txt_value_list))
                cur.execute("COMMIT")
        consumer.commit()
    except Exception as err:
        print(err)
    finally:
        consumer.close()


def lpr_consumer_img():
    img_value_list = {}
    consumer = Consumer(k_conf_info)
    try:
        consumer.subscribe([topic_img])
        running = True
        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                running = False
            else:
                img_value_list.update(
                    {msg.key().decode("utf-8"): msg.value().decode("utf-8")})
        for k, v in img_value_list.items():
            os.makedirs(os.path.dirname(lpr_server_data_path+k), exist_ok=True)
            with open(lpr_server_data_path+k, "wb") as fh:
                fh.write(base64.b64decode(v))
        consumer.commit()
    except Exception as err:
        print(err)
    finally:
        consumer.close()


if __name__ == "__main__":
    lpr_consumer_txt()
    lpr_consumer_img()
