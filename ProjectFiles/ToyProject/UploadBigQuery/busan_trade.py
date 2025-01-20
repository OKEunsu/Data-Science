from google.colab import auth
from google.cloud import bigquery
from google.cloud.exceptions import NotFound

import requests
import pandas as pd
import json
from google.colab import userdata

def upload_bigquery(table_name : str, page_no : str, num_page : str):
  service_key = userdata.get('key_2')
  
  # 사용자 인증
  auth.authenticate_user()

  # 여기서 YOUR_PROJECT_ID를 Google Cloud 프로젝트 ID로 교체하세요.
  project_id = 'spartacoding'
  client = bigquery.Client(project=project_id)

  # DataFrame을 BigQuery로 업로드
  # 여기서 YOUR_DATASET_NAME과 YOUR_TABLE_NAME을 실제 데이터셋 및 테이블 이름으로 교체
  dataset_id = 'mydataset'
  table_id = table_name

  # busantrade data set
  url = "http://apis.data.go.kr/6260000/EgMarketGoods2/getTradeCount2"

  params = {
      "serviceKey": service_key, 
      "pageNo": page_no,        
      "numOfRows": num_page,  
      "resultType" : "json"
  }

  response = requests.get(url, params=params)
  data = response.json()['response']['body']['items']['item']
  df = pd.json_normalize(data)

  table_ref = client.dataset(dataset_id).table(table_id)

  job = client.load_table_from_dataframe(df, table_ref)

  # 잡이 완료될 때까지 기다립니다.
  job.result()

  print("업로드 완료")
