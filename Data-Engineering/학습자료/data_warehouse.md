# 데이터 웨어하우스 설계
### 1. 데이터 웨어하우스 기초
- OLTP vs OLAP
- ETL 프로세스
- 데이터 품질 관리

<br/>

### 2. 차원 모델링
- 스타 스키마
- 스노우플레이크 스키마
- 팩트 테이블과 차원 테이블
- SCD(Slowly Changing Dirmensions)

<br/>

### 3. 데이터 마켓

---

## OLTP vs OLAP
데이터베이스 시스템을 이해하기 위해서는 OLTP와 OLAP의 개념을 확실히 아는 것이 중요합니다.  
이 두 시스템은 서로 다른 목적과 특성을 가지고 있어서, 각각의 장단점을 잘 이해하면 효과적인 데이터 관리가 가능해집니다.  

<br/>

### OLTP (Online Transsaction Processing)
OLTP는 우리가 일상적으로 마주하는 거의 모든 실시간 데이터 처리 시스템  
OLTP 특징
1. 실시간 특징: 밀리초 단위의 빠른 응답 시간
2. 작은 데이터 처리: 한 번에 소량의 데이터만 다룸
3. 높은 동시성: 수많은 사용자의 요청을 동시에 처리
4. 데잍터 정확성: ACID 특성을 준수하여 데이터 일관성 보장

<br/>

### OLAP (Online Analytical Processing)
OLAP는 의사결정을 위한 데이터 분석 시스템.  
기업의 경영진이 전략을 수립하거나,  
데이터 분석가가 트렌드를 파악할 때 사용

OLAP 특징  
1. 대용량 데이터 처리: 수 년간의 누적 데이터를 분석  
2. 복잡한 쿼리: 다차원 분석과 집계 연산을 수행
3. 읽기 위주: 데이터 수정보다는 조회가 주된 작업
4. 느린 응답 시간: 복잡한 연산으로 인해 수초에서 수분 소요

<br/>

### 두 시스템의 상호작용
실제 비즈니스 환경에서는 이 두 시스템이 다음과 같이 협력  
```
[ OLTP 시스템 ] → [ ETL 과정 ] → [ OLAP 시스템 ]
일일 거래 데이터 → 데이터 추출/변환/적재 → 분석용 데이터
(실시간 처리)      (주로 야간에 처리)         (전략적 분석)
```

<br/>

은행의 ATM에서 발생하는 모든 거래(OLTP)는 하루가 끝나면 중앙 데이터 웨어하우스로  
이관되어, 다음날 고객 행동 패턴 분석이나 금융 상품 기획(OLAP)에 활용됩니다.  
이렇게 두 시스템은 서로 다른 목적을 가지고 있지만, 효과적인 비즈니스 운영을 위해서는  
둘 다 필수적. OLTP는 일상적인 업무 처리를, OLAP는 전략적 의사결정을 지원하면서  
기업의 데이터 기반 의사결정을 가능하게 만듭니다.  

<br/>

## ETL 프로세스 
데이터 웨어하우스를 구축할 때 가장 중요한 과정인 ETL(Extract, Transform, Load)  

<br/>

### ETL 프로세스 기본구조
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/d03f6af8-096c-4d97-a0de-33512d283106" />

<br/>

### 각 단게별 상세 설명
#### 1. 추출(Extract) 단계
추출 단계는 여러 곳에서 필요한 데이터를 가져오는 과정.  
```
[데이터 소스별 추출 방식]
CRM 시스템 ➜ API 호출
ERP 시스템 ➜ 데이터베이스 쿼리
로그 파일 ➜ 파일 읽기
SNS 데이터 ➜ 웹 크롤링
```

<br/>

#### 2. 변환(Transform) 단계
변환 단게는 데이터를 사용 가능한 형태로 가공하는 단계.
```
[원본 데이터]
   ↓
[클렌징] → 오류 제거, 중복 제거  
   ↓
[표준화] → 형식 통일, 단위 변환  
   ↓
[보강] → 계산 수행, 파생 변수 생성  
   ↓
[통합] → 다양한 데이터 병합
```
예를 들어, 온라인 쇼핑몰의 경우:
- 상품 가격이 달러로 된 것을 원화로 변환
- 날짜 형식을 'YYYY-MM-DD'로 통일
- 주문량과 단가를 곱해 총 매출 계산
- 고객 정보와 주문 정보를 결합

<br/>

#### 3. 적재(Load) 단계
```
[적재 방식]
전체 적재:
기존 데이터 ➜ [삭제] ➜ 새 데이터 적재

증분 적재:
기존 데이터 ➜ [변경분 확인] ➜ 추가/수정
```

<br/>

#### 실제 적용 사례
대형 마트 체인 ETL 프로세스  

```
매일 밤 ETL 프로세스
23:00 ➜ 각 지점 POS 데이터 추출
23:30 ➜ 상품코드 표준화, 금액 계산
00:00 ➜ 데이터 웨어하우스 적재
01:00 ➜ 데이터 검증 완료
```
이렇게 처리된 데이터는 다음날 아침 경영진이 전국 매장의 판매 현황을 분석하는 데 사용됩니다.  
<br/>

#### 데이터 품질의 핵심 차원
데이터 품질은 여러 측면에서 평가되어야 함.  

| 차원명   | 설명                       |
|----------|----------------------------|
| 정확성   | 데이터가 사실과 얼마나 일치하는가 |
| 적시성   | 데이터가 얼마나 최신이고 시의적절한가 |
| 완전성   | 누락된 데이터 없이 충분한가 |
| 일관성   | 다른 데이터와 충돌 없이 일치하는가 |

<br/>

정확성은 은행 계좌 잔액
➜ 실제 보유한 금액이 정확하게 표시 되어야 하며,  
단 1원의 오차도 허용되지 않음  

<br/>

완전성은 퍼즐 맞추기  
➜ 한 조각도 없다면 전체 그림을 볼 수 없음  

<br/>

### 데이터 품질 관리 프로세스
실제 데이터 품질 관리는 순환적인 프로세스로 진행  
```
# 품질 관리 사이클

프로파일링 → 모니터링 → 정제 → 예방
↑                             ↓
└─────────────────────────────┘
          피드백 및 개선
```
예시: 대형 온라인 쇼핑몰  

<br/>

#### 프로파일링 단계
매주 월요일아침, 데이터 팀은 지난 주 주문 데이터를 검토  
배송 주소 형식이 올바른지, 결제 금액이 제품 가격과 일치하는지 등을 확인  

<br/>

#### 모니터링 단계
실시간으로 주문 데이터를 감시하는 시스템 운영

```
주문 데이터 모니터링

├── 이메일 형식 검증  
│   └── [사용자@도메인.com] 패턴 확인

├── 전화번호 형식 검증  
│   └── [000-0000-0000] 패턴 확인

└── 주소 정보 검증  
    └── [우편번호 + 기본주소 + 상세주소] 확인
```

<br/>

#### 정제 단계
발견된 문제를 해결
- 중복된 고객 계정 통합
- 오타가 있는 제품명 수정
- 표준화되지 않은 주소 형식 정리

<br/>

#### 예방 단계
문제의 재발을 방지하기 위한 시스템을 구축
- 데이터 입력 시 자동 검증 규칙 적용
- 직원 교육 프로그램 운영
- 데이터 품질 가이드라인 문서화

<br/>

## 차원 모델링
### 팩트 테이블
팩트 테이블은 비즈니스의 핵심 측정값을 조장하는 중심 테이블  
실제로 측정하고 싶은 모든 수치들  

<br/>
예시: 온라인 쇼핑몰의 판매 팩트 테이블
```
CREATE TABLE 판매_팩트 (
   주문ID INTEGER,
   제품ID INTEGER,
   고객ID INTEGER,
   날짜ID INTEGER,
   판매수량 INTEGER,
   판매금액 DECIMAL(10, 2),
   할인금액 DECIMAL(10, 2),
   순이익 DECIMAL(10, 2),
   FOREIGN KEY (제품ID) REFERENCES 제품_차원(제품ID),
   FOREIGN KEY (고객ID) REFERENCES 고객_차원(고객ID),
   FOREIGN KEY (날짜ID) REFERENCES 시간_차원(날짜ID)
); 
```

<br/>

### 차원 테이블의 상세 구조
차원 테이블은 우리가 데이터를 분석할 때 사용하는 다양한 관점을 제공  
```
CREATE TABLE 제품_차원 (
    제품ID INTEGER PRIMARY KEY,
    제품명 VARCHAR(100),
    카테고리 VARCHAR(50),
    브랜드 VARCHAR(50),
    제조사 VARCHAR(100),
    출시일자 DATE,
    단가 DECIMAL(10,2),
    재고단위 VARCHAR(20)
);
```

<br/>

### 이런 설계 방식은
- 스노우플레이크 스키마: 차원이 여러 관련 테이블로 정규화되는 스타 스키마의 확장입니다
- 스타 스키마: 중앙 팩트 테이블이 여러 차원 테이블로 둘러싸여 별 모양을 닮은 가장 단순하고 일반적인 스키마입니다
- SCD 스키마: 시간에 따른 차원 속성 데이터의 변화를 처리하는 기법입니다.

<br/>

### 데이터 아키텍처: 데이터 마켓
#### 데이터 레이크: 모든 데이터의 시작점
정제되지 않은 원시 데이터가 그대로 저장되는 거대한 저장소  

<br/>

#### 특징
```
# 데이터 레이크의 일반적인 구성 
data_lake_contents = {
    '구조화된_데이터': {
        'DB_백업': {
            'type': 'SQL dumps',
            'frequency': '일간',
            'retention': '영구'
        },
        '거래_기록': {
            'type': 'CSV files',
            'frequency': '실시간',
            'retention': '5년'
        }
    },
    '반구조화된_데이터': {
        '로그_파일': {
            'type': 'JSON/XML',
            'frequency': '실시간',
            'source': '웹서버, 앱서버'
        }
    },
    '비구조화된_데이터': {
        '고객_피드백': {
            'type': '텍스트, 이미지',
            'source': '이메일, SNS'
        }
    }
}
```
이런 원시 데이터는 추후 분석을 위한 귀중한 자원.  
데이터 생태계의 기반

<br/>

### 데이터 웨어하우스
데이터가 사용 목적에 맞게 정제되고 구조화

<br/>

#### 핵심 구성

```
-- 고객 정보 관리
CREATE TABLE customer_dimension (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    segment VARCHAR(50),
    lifetime_value DECIMAL(12,2),
    first_purchase_date DATE,
    last_purchase_date DATE,
    CONSTRAINT valid_dates CHECK (first_purchase_date <= last_purchase_date)
);

-- 거래 이력 관리
CREATE TABLE transaction_fact (
    transaction_id BIGINT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    transaction_date TIMESTAMP,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customer_dimension(customer_id)
);
```
이러한 구조화된 데이터는 기업의 의사결정을 위한 기반

<br/>

### 데이터 마트
목적에 특화된 데이터 제공
각 부서나 팀의 특정 요구사항에 맞춰진 작은 규모의 데이터 웨어하우스  

<br/>

#### 부서별 데이터 마트 예시
```
CREATE VIEW marketing_campaign_performance AS
SELECT
    c.segment AS customer_segment,
    COUNT(DISTINCT t.customer_id) AS unique_customers,
    SUM(t.amount) AS total_revenue,
    AVG(t.amount) AS average_order_value
FROM transaction_fact t
JOIN customer_dimension c ON t.customer_id = c.customer_id
WHERE t.transaction_date >= CURRENT_DATE - INTERVAL '90 days'
GROUP BY c.segment;
```








