## 목차
- MVC, MFV
- Django 개념
- Projcet와 App
- settings.py
- manage.py
<br/>

### MVC & MTV
- Model : 안전하게 데이터를 저장
- View : 데이터를 적절하게 유저에게 보여줌
- Control, Template(Django) : 사용자의 입력과 이벤트에 반응하여 Model과 View를 업데이트
<br/>

## Settings.py
프로젝트 환경 설정 파일
- DEBUG : 디버그 모드 설정
- INSTALLED_APPS : PIP로 설치한 앱 또는 본인이 만든 APP을 추가
- MIDDELWARE_CLASSES : REQUEST와 RESPONSE 사이의 주요 기능 레이어
- TEMPLATES : DJANGO TEMPLATE관련 설정, 실제 뷰(HTML, 변수)
- DATABASES : 데이터 베이스 엔진의 연결 설정
- STATIC_URL : 정적 파일의 URL(CSS, JAVASCRIPT, IMAGE, ETC)
<br/>

### Manage.py
- 프로젝트 관리 명령어 모음
- 주요 명령어
    - startapp - 앱생성
    - runserver - 서버 실행
    - createsuperuser - 관리자 생성
    - makemigrations app -app의 모델 변경 사항 체크
    - migrate - 변경 사항을 db에 반영
    - shell - 셀을 통해 데이터를 확인
    - collectstatic - static 파일을 한 곳에 모음
<br/>

## Contents
1. 프로젝트 & app 생성
2. 디렉토리 구조 확인
3. 관리자 페이지 확인
4. 글쓰기
5. 리스트
6. 글 보기
<br/>

# 장고 설치
```python
pip install django
```
<br/>

# 장고 버젼 확인
```python
django-admin --version
```
<br/>

# 장고 프로젝트 생성하기
```python
django-admin startproject [projectname]
```
<br/>

# 장고 프로젝트 내 앱 생성하기
```python
python manage.py startapp polls
```
<br/>

# 파일 구조 
```python
tree /F
```
<br/>

# 마이그레이션 적용
```python
python manage.py migrate
```
<br/>

# 관리자계정 생성
```python
python manage.py createsuperuser
```
<br/>

```
Username (leave blank to use 'wd'): admin
Email address: admin@naver.com
Password: 1234
Password (again): 1234
```
<br/>

# 개발 서버 실행
```python
python manage.py runserver
```
<br/>

# 서버 포트 변경
```python
python manage.py runserver 8080
```
<br/>

# 애플리케이션 생성
```python
python manage.py startapp [application name]
```
<br/>

# 생성 후 setting.py
INSTALLED_APPS 에 추가

# models.py
```python
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)
```
<br/>

# 모델 추가 후
## 마이그레이션 파일 탐색
```python
python manage.py makemigrations
```
<br/>

## 데이터베이스 업데이트
```python
python manage.py migrate
```
