# 스키마(Schema)
스키마는 데이터베이스의 전체적인 구조와 규칙을 정의하는 포괄적인 청사진입니다.  
실제 건축에서 설계도가 건물의 모든 세부 사항을 정의하는 것처럼, 스키마는 데이터베이스의 구조를 정의합니다. 
MySQL에서는 데이터베이스와 같은 개념으로 생각할 수 있습니다. 


# 스키마의 세 가지 차원 

## 1. 개념적 스키마:

조직의 데이터 구조를 가장 추상적인 수준에서 표현합니다.  
온라인 쇼핑몰의 예시: 'Sales', 'Inventory', 'Customer', 'Marketing'과 같은 비즈니스 영역별 스키마를 정의할 수 있습니다.  
이는 백화점의 각 층이 특정 상품군을 판매하는 것과 비슷한 개념입니다.  

```sql
-- 예시:
CREATE SCHEMA Sales;
CREATE SCHEMA Inventory;
CREATE SCHEMA Customer;
CREATE SCHEMA Marketing;
```

## 2. 논리적 스키마:  

실제 데이터 모델을 정의합니다.  
다음과 같이 구체화될 수 있습니다.  

```sql
-- 예시:
-- 고객 기본 정보 관리
CREATE TABLE Customer.BasicInfo(
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);
-- 고객 주소 정보 관리
    CREATE TABLE Customer.Address (
    address_id INT PRIMARY KEY,
    customer_id INT,
    address_type VARCHAR(20),
    street VARCHAR(255)
);

```
Customer 스키마 안에 BasicInfo와 Address 테이블을 생성하여 고객 기본 정보 및 주소 정보를 관리할 수 있습니다. 


```SQL
CREATE SCHEMA Customer;

CREATE TABLE Customer.BasicInfo (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);

CREATE TABLE Customer.Address (
    address_id INT PRIMARY KEY,
    customer_id INT,
    address_type VARCHAR(20),
    street VARCHAR(255)
);

```

<br/>

## 3. 물리적 스키마:

실제 데이터가 저장되는 방식을 정의합니다. 

테이블스페이스를 정의하여 전용 저장 공간을 만들고, 데이터 파일의 초기 크기, 자동 확장 여부 등을 설정할 수 있습니다. 


MySQL은 테이블 단위로 스토리지 엔진을 선택할 수 있으며, 일반적으로 InnoDB가 사용됩니다. 

```SQL

CREATE TABLESPACE customer_data
    DATAFILE 'customer.dat'
    SIZE 100M
    AUTOEXTEND ON;

ALTER TABLE Customer.BasicInfo
    TABLESPACE customer_data
    STORAGE (
        INITIAL 50M
        NEXT 50M
        MAXEXTENTS UNLIMITED
    );
```

<br/>

---

## 스키마의 보안과 접근 제어 

스키마는 데이터 보안의 첫 번째 방어선 역할을 합니다.  
특정 사용자에게 특정 스키마 또는 테이블에 대한 권한을 부여하여 접근을 제어할 수 있습니다.  


```SQL
-- 사용자 생성
CREATE USER 'marketing_team'@'localhost'
IDENTIFIED WITH mysql_native_password
BY 'password123';
```

<br/>

```sql
-- 권한 부여
GRANT SELECT ON Customer.BasicInfo
To 'marketing_team'@'localhost';
```

<br/>

```sql
-- 권한 내용: SELECT, UPDATE
GRANT SELECT, UPDATE ON Customer.Address
TO 'customer_service'@'localhost';
```

<br/>

```sql
-- 권한 변경 사항 적용
FLUSH PRIVILEGES;
```

<br/>

```sql
-- 최소 권한 부여
GRANT USAGE ON *.* TO `customer_service`@`localhost`;
-- 계정만 있음
-- 잠금 계정
```

<br/>

## 스키마 간의 관계와 의존성 

스키마는 서로 독립적이면서도 연결될 수 있습니다. 예를 들어, 
Sales 스키마의 Orders 테이블은 Customer 스키마의 BasicInfo 테이블과 
customer_id를 통해 외래 키(FOREIGN KEY) 관계로 연결될 수 있습니다. 


```sql
CREATE TABLE Sales.Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customer.BasicInfo (customer_id)
);
```
- PK: 모든 레코드에서 서로 다른 레코드
    - 중복 불가
    - null 존재 불가
    - 기본은 하나의 기본키, 복수도 가능
  
<br/>

## 스키마 진화와 유지보수 

스키마는 비즈니스 요구사항의 변화에 따라 진화할 수 있어야 합니다.  
새로운 컬럼을 추가하거나, 새로운 비즈니스 영역을 위한 스키마를 추가하여 확장할 수 있습니다.  

```SQL
-- 새로운 기능을 위한 스키마 확장
ALTER TABLE Customer.BasicInfo
ADD COLUMN loyalty_level VARCHAR(20);

-- 새로운 비즈니스 영역을 위한 스키마 추가
CREATE SCHEMA Analytics;
CREATE TABLE Analytics.CustomerBehavior (
    customer_id INT,
    session_date DATE,
    activity_type VARCHAR(50)
);
```
<br/>

---
# 잘 설계된 스키마란?

데이터베이스 스키마는 데이터베이스의 논리적 구조를 정의하는 청사진으로,
테이블, 열, 관계, 인덱스, 제약 조건 등을 포함하여 데이터베이스의 전체적인 구조를 나타낸다. 
잘 설계된 스키마는 시스템의 성능, 확장성, 유지보수성에 직접적인 영향을 미치며, 다음과 같은 핵심 요소들을 만족해야 한다.

## 1. 논리적 구조화
현실 세계의 정보를 체계적으로 데이터베이스로 변환하는 과정이다. 이 과정에서는 다음과 같은 개념이 중요하다:

- 엔티티(Entity): 현실세계의 객체를 추상화한 것으로, 테이블의 이름이 된다.
- 속성(Attribute): 엔티티를 구성하는 데이터 항목으로, 테이블의 열(Column)이 된다.

개념적 설계 단계에서는 ERD 다이어그램을 통해 엔티티 간 관계를 시각화하고, 
논리적 설계 단계에서 테이블, 속성, 기본키, 외래키로 구체화한다.

<br/>

## 2. 의미적 일관성 유지

모든 속성은 그에 맞는 엔티티 안에 포함되어야 하며, 
의미적으로 관련된 속성들은 같은 테이블에 배치해야 한다. 
속성의 위치가 부자연스럽거나 데이터가 중복된다면 이는 구조상의 문제가 있다는 신호일 수 있다. 
의미적 일관성을 지키면 데이터 중복을 줄이고 조인 시 오류 발생 가능성을 줄일 수 있다.

<br/>

## 3. 데이터 정규화
정규화는 데이터 중복을 최소화하고 데이터 무결성을 보장하기 위한 테이블 분해 및 재구성 과정이다.

- 제1정규형(1NF): 모든 컬럼이 원자값만 갖도록 한다. 다중값 컬럼은 분리되어야 한다.
- 제2정규형(2NF): 1NF를 만족하면서, 기본키의 일부가 아닌 속성은 전체 기본키에 종속되어야 한다.
- 제3정규형(3NF): 2NF를 만족하고, 모든 속성이 기본키에 직접 종속되어야 한다. 전이적 종속성을 제거한다.

정규화를 통해 데이터 삽입, 삭제, 갱신 시 발생하는 이상현상을 예방할 수 있다.

<br/>

## 4. 명확한 관계 정의
관계형 데이터베이스에서 테이블 간 관계는 다음과 같은 유형으로 정의된다:
- 일대일 (1:1): 각 레코드가 다른 테이블의 하나의 레코드와만 연결된다. 예: 국가-수도
- 일대다 (1:N): 하나의 레코드가 여러 개의 다른 테이블 레코드와 연결된다. 예: 고객-주문
- 다대다 (N:M): 여러 개의 레코드가 서로 다수와 연결된다. 이 경우 중간 테이블(연결 테이블)을 사용해 두 개의 1:N 관계로 나눈다.

관계를 명확히 정의하면 데이터 중복을 줄이고, 무결성과 확장성을 확보할 수 있다.

<br/>

## 5. 확장성 고려

데이터베이스는 시간이 지나며 요구사항이 바뀌고 데이터 양이 증가하므로, 확장 가능한 설계를 미리 고려해야 한다.  
Primary Key에 의미를 부여하지 말 것: 단순히 식별자로만 사용해야 하며, 의미를 부여하면 재설계가 필요해질 수 있다.  
NULL 허용 여부 신중하게 판단: 수집이 불가능하거나 선택적으로 입력되는 속성은 NULL 허용을 고려해야 한다.  
현재만 고려한 컬럼 생략 지양: 미래의 기능 추가 가능성을 고려하여 구조를 유연하게 설계해야 한다.  
관계형 데이터베이스에서는 파티셔닝을 통해 데이터 테이블을 연도별, 지역별 등으로 나누어 관리하고,   
NoSQL 시스템에서는 수평 확장을 통해 서버를 늘려 성능을 향상시킬 수 있다.  

<br/>

## 6. 성능 최적화
잘 설계된 스키마는 효율적인 쿼리를 유도하고 시스템 리소스를 절약해야 한다.  
데이터 타입 최적화: 가능한 한 작은 크기의 타입을 사용하고,  
복잡한 연산을 줄이기 위해 단순한 타입을 사용한다. 예: INT 대신 TINYINT, TEXT 대신 VARCHAR  
NULL 최소화: NULL은 쿼리 연산 및 인덱싱 시 성능을 저하시킬 수 있으므로 가급적 피한다.  
인덱싱 전략: 검색 성능을 높이기 위해 자주 조회되는 컬럼에 인덱스를 생성한다. 예: B-Tree 인덱스, 비트맵 인덱스  
클러스터링: 자주 조인되거나 함께 조회되는 테이블을 물리적으로 인접하게 저장하여 디스크 I/O를 최소화한다.  

<br/>

## 7. 데이터 보안
데이터베이스에 저장된 정보를 보호하기 위한 보안 설계가 필요하다.
- 접근 제어: 사용자의 권한에 따라 데이터 접근을 제어한다. 예: SELECT, INSERT, UPDATE, DELETE 권한 부여
- View 활용: 민감한 정보는 뷰(View)를 통해 필터링된 데이터만 제공한다
- 암호화: 민감한 데이터(예: 주민등록번호, 계좌번호)는 저장 시 암호화 처리한다
- 정보 흐름 제어: 시스템 외부로 중요한 정보가 유출되지 않도록 관리한다
- 추론 방지: 간접적인 정보 추론을 방지하기 위해 민감한 데이터는 분리 저장한다
- 보안 정책 모델에는 다음과 같은 유형이 있다:
- 임의적 접근 제어(DAC): 사용자 기반 권한 제어. GRANT/REVOKE 사용
- 강제적 접근 제어(MAC): 보안 등급 기반 제어. 고급 보안이 요구되는 시스템에 적합
- 역할 기반 접근 제어(RBAC): 역할(직무, 부서 등)에 따라 접근 권한을 정의. 다중 사용자 환경에 유리

<br/>

## 결론

잘 설계된 데이터베이스 스키마는 논리적 구조화, 의미적 일관성, 정규화, 명확한 관계 설정,  
확장성과 성능 최적화, 데이터 보안 체계를 모두 갖춘 구조이다.  
이러한 설계 원칙을 따르는 스키마는 데이터 무결성을 보장하고 유지보수성을 높이며,  
변화하는 비즈니스 요구사항에도 유연하게 대응할 수 있는 안정적인 시스템 기반을 제공한다. 
