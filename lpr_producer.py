import glob
import sys
import base64
from confluent_kafka import Producer
from lpr_common import k_conf_info, topic_img, topic_txt, lpr_edge_data_path


def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        sys.stderr.write('%% Message delivered to %s [%d] @ %d\n' %
                         (msg.topic(), msg.partition(), msg.offset()))


def lpr_producer():
    producer = Producer(k_conf_info)
    try:
        # produce txt file
        for filename in glob.iglob(lpr_edge_data_path + '**/*.txt', recursive=True):
            with open(filename, 'r') as txt:
                content = txt.read()
                print(hash(content))
                producer.produce(topic_txt, key=str(hash(content)),
                                 value=content, callback=delivery_callback)
                producer.poll(0)
        # produce img file
        for filename in glob.iglob(lpr_edge_data_path + '**/*.jpg', recursive=True):
            with open(filename, 'rb') as img:
                content = base64.b64encode(img.read())
                producer.produce(topic_img, key=filename[len(lpr_edge_data_path)-1:len(filename)],
                                 value=content, callback=delivery_callback)
                producer.poll(0)
    except Exception as err:
        print("Error "+str(err))
    finally:
        producer.flush()


if __name__ == "__main__":
    lpr_producer()
