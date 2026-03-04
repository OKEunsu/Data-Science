
# 🏨 소노캄 거제 리뷰 분석 프로젝트

## 📌 프로젝트 개요

- **목표**: 소노캄 거제 호텔에 대한 리뷰 데이터를 수집 및 분석하여 전반적인 고객 만족도와 개선점을 파악
- **데이터 출처**: 구글 리뷰 데이터 (`Rawdata.csv`)
- **사용 도구**: Python (NLTK, Pandas, Matplotlib, WordCloud)

---

## 📊 분석 프로세스

### 1. 데이터 전처리

- 컬럼명 및 타입 정제 (`Current score` → int)
- 리뷰 소문자 변환, 특수문자 제거, 불용어 제거, 표제어 추출 등 NLP 전처리 수행
- `"Translated by Google"` 등 불필요 문구 제거

```python
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in stopwords.words("english")]
    tokens = [WordNetLemmatizer().lemmatize(token) for token in tokens]
    return " ".join(tokens)
```

---

### 2. 단어 빈도 분석

- 전체 리뷰 텍스트 토큰화 및 단어 빈도 분석
- **상위 단어**: `good`, `view`, `clean`, `room` 등 → 전반적으로 긍정적 이미지

#### 📌 워드클라우드 시각화

```python
wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(top_50)
```

---

### 3. 평점 분석

- 평균 평점: **4.366점**
- 대부분 평점 **4~5점**에 집중

```python
df['current_score'].mean()  # 4.366
```

---

### 4. 부정적 리뷰 분석 (평점 1~2점)

- 대표 키워드: `dirty`, `service`, `expensive`, `noise`, `staff`
- 종합 의견: **청소**, **직원 태도**, **소음**, **가격 불만** 등이 주된 이슈

| 평점 | 주요 불만 내용 |
|------|----------------|
| 1~2점 | 체크인 대기, 샤워타월 미지급, 청소 미흡, 불친절, 시설 미흡, 가격 과다 등 |

---

### 5. 감성 분석

- 감성사전(SentiWordNet)을 활용하여 긍/부정 점수 계산
- 긍정 리뷰 비율이 월등히 높았으나, 일부 긍정 평점 리뷰에서도 부정 키워드 다수 존재

```python
def sentiment_analysis(sentence):
    ...
    return 1 / -1 / 0
```

#### 🔍 부정 리뷰 중 점수 높은 항목 분석
- 평점은 낮고 부정 점수도 높은 리뷰에 집중해 주요 이슈 확인
- 정량 기반으로 **서비스 개선 포인트 도출**

---

## 💬 인사이트 요약

### 🙁 부정 리뷰에서의 문제점

- **직원 태도 및 응대**에 대한 불만 다수
- **소음, 청소, 시설 상태** 관련 이슈 반복
- 성수기 대비 고객 응대 준비 부족

### 🙂 긍정 리뷰의 주요 요소

- **풍경, 산책로, 바다 전망** 등의 자연 요소 만족도 높음
- 일부 시설(카페, 주차장 등)은 긍정적으로 평가됨

---

## ✅ 결론 및 제안

- **직원 서비스 교육 강화 및 인력 보강** (성수기 대비)
- **청소 및 위생 상태 개선**
- **객실 구조 개선** (예: 에어컨 위치)
- **성수기/비수기 리뷰 분리 분석**으로 시기별 문제점 정밀 진단 필요
- 리뷰 텍스트 내 긍정 평점임에도 **부정 키워드가 포함된 경우 존재** → 감성분석 기반 NPS 개선 필요

---

## 🗂️ 프로젝트 파일 구성

- `소노캄 거제.ipynb`: 전체 분석 노트북
- `Rawdata.csv`: 리뷰 원본 데이터
- `README.md`: 프로젝트 요약 문서

---

## 🔗 참고 이미지 및 시각화

- 전체 리뷰 워드클라우드
- 평점별 분포 히스토그램
- 부정 리뷰 전용 워드클라우드
- 감성 점수 분포 시각화

---
