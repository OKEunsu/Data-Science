# 부산 거래 데이터 → BigQuery 적재

공공데이터포털의 부산 거래 데이터 API(`6260000/EgMarketGoods2/getTradeCount2`)에서 받은 JSON을 DataFrame으로 펼쳐 BigQuery 테이블에 올리는 Colab 스크립트입니다.

## 동작

`upload_bigquery(table_name, page_no, num_page)`

1. Colab에서 Google 계정 인증 후 BigQuery 클라이언트 생성 (프로젝트 `spartacoding`)
2. API를 `pageNo`·`numOfRows`·`resultType=json`으로 호출
3. `response.body.items.item`을 `pd.json_normalize`로 표 형태로 변환
4. `mydataset.{table_name}` 테이블에 적재하고 작업 완료까지 대기

## 실행

- Google Colab 전용 (`google.colab.auth`, `google.colab.userdata` 사용)
- API 인증키는 Colab 보안 비밀에 `key_2` 이름으로 등록해 읽는다. 코드에 키를 적지 않는다.
- 프로젝트 ID와 데이터셋 이름은 본인 환경에 맞게 바꾼다.

## 빅쿼리 적재 예시화면

![부산](https://github.com/user-attachments/assets/d530b676-9bed-4a31-b2c3-059f54084714)
