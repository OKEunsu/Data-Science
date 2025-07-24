
# 📦 부산 무역 데이터 BigQuery 적재 프로젝트

본 프로젝트는 공공 API로부터 부산 무역 데이터를 수집하여, 전처리 및 Google BigQuery에 적재하는 과정을 자동화한 Python 스크립트입니다.

---

## 📌 주요 기능

- [x] 공공 API에서 페이지 단위로 데이터 수집
- [x] pandas 데이터프레임으로 변환 및 전처리
- [x] Google BigQuery 테이블로 업로드 자동화

---

## 🛠 사용 기술

- Python 3.x
- Pandas
- Google Cloud BigQuery (google-cloud-bigquery)
- 공공데이터포털 API

---

## 📁 파일 구조

```
busan_trade.py        # 전체 적재 스크립트
```

---

## 🧪 함수 설명

### `upload_bigquery(table_name: str, page_no: str, num_page: str)`

> 공공 API에서 데이터를 수집하고 BigQuery에 적재하는 핵심 함수입니다.

| 파라미터     | 타입 | 설명                                      |
|--------------|------|-------------------------------------------|
| table_name   | str  | 업로드할 BigQuery 테이블 이름             |
| page_no      | str  | API 요청 시작 페이지 번호 (1부터 시작)    |
| num_page     | str  | 한 번에 가져올 페이지 수                  |

```python
def upload_bigquery(table_name: str, page_no: str, num_page: str):
    ...
```

---

## 🧾 실행 예시

```bash
python busan_trade.py
```

또는 Jupyter 환경에서 함수 실행:

```python
upload_bigquery(
    table_name='project.dataset.busan_trade',
    page_no='1',
    num_page='10'
)
```

---

## ✅ BigQuery 테이블 예시

| year | region | hs_cd | hs_nm  | value |
|------|--------|-------|--------|-------|
| 2024 | 부산   | 2710  | 석유제품 | 30000 |

---

## 🔑 GCP 인증 필요

GCP 인증을 위해 서비스 계정 키(`.json`)를 사용해야 하며, 환경 변수로 설정해야 합니다.

```bash
export GOOGLE_APPLICATION_CREDENTIALS="your_service_account.json"
```

---

## 📝 추가 사항

- 에러 처리, 중복 제거 등은 필요 시 커스터마이징
- BigQuery에 테이블이 없을 경우 자동 생성됨
- API 한계에 따라 `num_page` 설정을 적절히 조절

---

## 빅쿼리 적재 예시화면
![부산](https://github.com/user-attachments/assets/d530b676-9bed-4a31-b2c3-059f54084714)
