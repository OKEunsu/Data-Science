# 스키마(Schema)
스키마는 데이터베이스의 전체적인 구조와 규칙을 정의하는 포괄적인 청사진입니다.  
실제 건축에서 설계도가 건물의 모든 세부 사항을 정의하는 것처럼, 스키마는 데이터베이스의 구조를 정의합니다. 
MySQL에서는 데이터베이스와 같은 개념으로 생각할 수 있습니다. 


스키마의 세 가지 차원 

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

## 물리적 스키마:

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

스키마의 보안과 접근 제어 

스키마는 데이터 보안의 첫 번째 방어선 역할을 합니다. 특정 사용자에게 특정 스키마 또는 테이블에 대한 권한을 부여하여 접근을 제어할 수 있습니다. 


```SQL

CREATE USER 'marketing_team'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password123';
GRANT SELECT ON Customer.BasicInfo TO 'marketing_team'@'localhost';
```

스키마 간의 관계와 의존성 

스키마는 서로 독립적이면서도 연결될 수 있습니다. 예를 들어, 

Sales 스키마의 Orders 테이블은 Customer 스키마의 BasicInfo 테이블과 customer_id를 통해 외래 키(FOREIGN KEY) 관계로 연결될 수 있습니다. 


```sql

CREATE TABLE Sales.Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customer.BasicInfo (customer_id)
);
```
스키마 진화와 유지보수 

스키마는 비즈니스 요구사항의 변화에 따라 진화할 수 있어야 합니다. 새로운 컬럼을 추가하거나, 새로운 비즈니스 영역을 위한 스키마를 추가하여 확장할 수 있습니다. 


```SQL

ALTER TABLE Customer.BasicInfo
ADD COLUMN loyalty_level VARCHAR(20);

CREATE SCHEMA Analytics;
CREATE TABLE Analytics.CustomerBehavior (
    customer_id INT,
    session_date DATE,
    activity_type VARCHAR(50)
);```
잘 설계된 스키마란? 

논리적 구조화 

데이터 정규화 

명확한 관계 정의 

확장성 고려 

성능 최적화 

데이터 보안 
