# lpr_code

# 環境需求
  ## python 3.8
  ## 安裝套件
    pip3 install -r requirements.txt
# 參數設定
  ## 請參考 lpr_common.py
  ## Edge端
    Kafka位置
    Edge端檔案路徑
  ## Server端
    Kafka位置
    Vertica連線資訊
    Server端檔案路徑
# 執行
  ## Edge端
  ### python3 -m lpr_producer
  ## Server端
  ### python3 -m lpr_consumer
  
# Table 結構

  ~~~
  create table public.MITAC_DEMO(
	  cctv_id varchar(20),
	  car_id varchar(20),
	  record_timestamp varchar(14),
	  v_type varchar(2)
  )
 
