## 파이썬 GSheet
## API 사용등록

![image](https://github.com/user-attachments/assets/e961b26d-c58e-4d8a-9b6d-1a5b950e542e)


### 사용자 인증 정보 만들기

- 사용자 인증 정보 만들기 → 서비스 계정
- 편집자 or 소유자로 입력해야 모든 권한 접근 가능
- 계정 키 Json 만들기

### 구글시트에 api 계정 등록

### 파이썬 코드

```
# 패키지 설치
pip install gspread
```

```python
import pandas as pd
import gspread

gc = gspread.service_account(filename='your_api_key.json')
sh = gc.open('연습용').worksheet('시트1')
print(sh.get('A1')) # a1 값 가져오기

# 모든 데이터 가져오기
data = sh.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])
print(df)

# 데이터 쓰기
sh.update_acell('B2', 'example Name')
print(sh.get('B2'))
```

## Ref

[Connect Streamlit to a private Google Sheet - Streamlit Docs](https://docs.streamlit.io/develop/tutorials/databases/private-gsheet)

# Streamlit Gsheet Database

→ streamlit cloud에 배포할때 csv파일을 같이 올렸는데 파일연결이 안되서 방법을 찾음

```
pip install streamlit
pip install st-gsheets-connection 
```

https://github.com/streamlit/gsheets-connection

### Gsheet 연결은 두가지 방법

- 읽기 전용 모드에서 공개적으로 공유된 스프레드 시트 URL 사용(읽기 전용 모드)
- 서비스 계정을 사용한 인증 GRUD 작업 지원 모드(**API 사용등록)**

### 읽기 전용

```python
# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)
```

### 서비스계정/CRUD

1. .streamlit/secrets.toml
2. Google Drive API. Google Sheets API 활성화
3. 키 json 발급

```
{
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
    ...
}
```

1. .streamlit/secrets.toml 파일 생성

```
# .streamlit/secrets.toml

[connections.gsheets]
spreadsheet = "<spreadsheet-name-or-url>"
worksheet = "<worksheet-gid-or-folder-id>"  # worksheet GID is used when using Public Spreadsheet URL, when usign service_account it will be picked as folder_id
type = ""  # leave empty when using Public Spreadsheet URL, when using service_account -> type = "service_account"
project_id = ""
private_key_id = ""
private_key = ""
client_email = ""
client_id = ""
auth_uri = ""
token_uri = ""
auth_provider_x509_cert_url = ""
client_x509_cert_url = ""
```

```python
# example/st_app_gsheets_using_service_account.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read Google Sheet as DataFrame")

conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Example 1")

st.dataframe(df)
```

## 로컬 환경에서 사용

toml파일을 안쓰고 json파일 그대로 이용

```python
def get_google_sheet():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('your_api_key.json', scope)
    client = gspread.authorize(creds)
    return client.open('file_name').worksheet('sheet_name')
```

## Streamlit Cloud toml 사용법

1. URL, toml 기입

```python
# .streamlit/secrets.toml
[connections.gsheets]
spreadsheet = "GoogleSheetSharingURL"

# My JSON key file
[connections.gsheets]
spreadsheet = "<spreadsheet-name-or-url>"
worksheet = "<worksheet-gid-or-folder-id>"  # worksheet GID is used when using Public Spreadsheet URL, when usign service_account it will be picked as folder_id
type = ""  # leave empty when using Public Spreadsheet URL, when using service_account -> type = "service_account"
project_id = ""
private_key_id = ""
private_key = ""
client_email = ""
client_id = ""
auth_uri = ""
token_uri = ""
auth_provider_x509_cert_url = ""
client_x509_cert_url = ""
```

![image](https://github.com/user-attachments/assets/fda6a263-2e30-4314-b533-39727c0517c2)
