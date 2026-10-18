# Pixabay 이미지 크롤러

키워드로 Pixabay 한국어 페이지를 검색해 결과 이미지를 내려받는 Selenium 스크립트입니다.

## 동작

1. `https://pixabay.com/ko/images/search/{키워드}`에 접속해 마지막 페이지 번호를 읽는다.
2. 페이지 끝까지 스크롤해 지연 로딩된 이미지를 모두 불러온 뒤 이미지 주소를 모은다 (`blank.gif` 자리표시 제외).
3. `img/{키워드}/{키워드}_{페이지}_{순번}.jpg`로 저장한다. 다운로드마다 1초 쉰다.
4. 지정한 페이지 수(기본 10)와 실제 마지막 페이지 중 작은 쪽까지 반복한다.

## 실행

```bash
pip install selenium chromedriver-autoinstaller requests
python pixabay_crawler.py   # 예시 키워드: 바나나
```

## 한계

- 페이지 요소를 절대 XPath와 자동 생성 클래스명(`cell--UMz-x`)으로 찾는다. Pixabay 화면 구조가 바뀌면 동작하지 않는다.
- 다음 페이지 주소를 `{검색 URL}&pagi=N`으로 만든다. 검색 URL에 `?`가 없어 2페이지 이후 이동이 의도대로 되는지 확인이 필요하다.
