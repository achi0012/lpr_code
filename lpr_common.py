# ./kafka-topics.sh --delete --bootstrap-server 192.168.100.13:9092 --topic LPR_IMG
# ./kafka-topics.sh --delete --bootstrap-server 192.168.100.13:9092 --topic LPR_TXT
# ./kafka-topics.sh --list --bootstrap-server 192.168.100.13:9092

# Vertica Connection Infomation
v_conn_info = {"host": "192.168.100.10",
               "port": 5433,
               "user": "dbadmin",
               "password": "achi0012",
               "database": "bp",
               # autogenerated session label by default,
               "session_label": "lpr",
               # default throw error on invalid UTF-8 results
               "unicode_error": "replace",
               # SSL is disabled by default
               "ssl": False,
               # autocommit is off by default
               "autocommit": True,
               # using server-side prepared statements is disabled by default
               "use_prepared_statements": True,
               # connection timeout is not enabled by default
               # 5 seconds timeout for a socket operation (Establishing a TCP connection or read/write operation)
               "connection_timeout": 5}

target_table = "public.MITAC_DEMO"

# Kafka Connection Information
# 192.168.100.13:9092,192.168.100.14:9092
k_conf_info = {"bootstrap.servers": "192.168.100.13:9092",
               "group.id": "lpt_dev",
               "session.timeout.ms": 10000,
               "auto.offset.reset": "earliest",
               "enable.auto.commit": False}

topic_txt = "LPR_TXT"
topic_img = "LPR_IMG"

# Data path on edge
lpr_edge_data_path = "/opt/lpr/edge_data/"

# Data path on Server
lpr_server_data_path = "/opt/lpr/server_data/"
