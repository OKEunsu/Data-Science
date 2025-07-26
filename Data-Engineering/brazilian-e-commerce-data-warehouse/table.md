# 테이블의 상세 구조
테이블은 데이터를 저장하는 기본 단위이지만, 테이블을 만들 때는 중요한 요소들을 고려해야 한다.

## 1. 데이터 타입
각 열은 특정 데이터 타입을 가져야 합니다. 

<br/>

```sql
CREATE TABLE Mebership.Members (
  memeber_id INT PRIMARY KEY, 
  name VARCHAR(50) NOT NULL,
  birth_date DATE,
  point_balance DECIMAL(10, 2),
  is_active BOOLEAN DEFAULT true,
  registration_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Members 테이블: 회원 기본 정보를 저장하는 테이블
CREATE TABLE Membership.Members (
  member_id SERIAL PRIMARY KEY, -- 회원 고유 식별자 (자동 증가 시퀀스 사용)
  name VARCHAIR(50) NOT NULL, -- 회원이름 (필수 입력, 최대 50자)
  birth_date DATE, -- YYYY-MM-DD 형식
  point_balance DECIMAL(10, 2) DEFAULT 0.00, -- 포인트 잔액 (소수점 둘째 자리까지 허용)
  is_active BOOLEAN DEFAULT true, -- 계정 활성화 상태 (기본값: 활성화)
  registration_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 가입 일시 (자동 기록)
  last_login_at TIMESTAMP, -- 마지막 로그인 시간
  email VARCHAR(100) UNIQUE, -- 이메일 (고유값 보장)
  phone VARCHAR(20) CHECK (phone ~ '^[0-9\-\+]+$']) -- 연락처 (정규식으로 형식 검증)
);

-- 테이블에 대한 설명 추가
COMMENT ON COLUMN Membership.Members.member_id IS '회원 고유 식별 번호';
COMMENT ON COLUMN Membership.Members.name IS '회원 이름';
COMMENT ON COLUMN Membership.Members.birth_date IS '생년월일';
```
<br/>

### 주요 데이터 타입, 용도
#### 숫자 타입
| 타입             | 설명                                       |
| -------------- | ---------------------------------------- |
| `SERIAL`       | 자동 증가하는 정수 (1, 2, 3, ...)                |
| `INT`          | 일반 정수 (-2,147,483,648 \~ +2,147,483,647) |
| `SMALLINT`     | 작은 범위의 정수 (-32,768 \~ +32,767)           |
| `DECIMAL(p,s)` | 정확한 소수. `p`: 전체 자릿수, `s`: 소수점 이하 자릿수     |
| `FLOAT`        | 부동 소수점. 큰 범위 표현 가능하나 정확도는 떨어질 수 있음       |

#### 문자열 타입
| 타입           | 설명                        |
| ------------ | ------------------------- |
| `CHAR(n)`    | 고정 길이 문자열. 남은 공간은 공백으로 채움 |
| `VARCHAR(n)` | 가변 길이 문자열. 최대 n자까지 저장 가능  |
| `TEXT`       | 길이 제한이 없는 긴 텍스트 저장에 적합    |

#### 시간 관련 타입
| 타입          | 설명                                        |
| ----------- | ----------------------------------------- |
| `DATE`      | 날짜만 저장 (형식: YYYY-MM-DD)                   |
| `TIME`      | 시간만 저장 (형식: HH\:MM\:SS)                   |
| `TIMESTAMP` | 날짜와 시간을 함께 저장 (형식: YYYY-MM-DD HH\:MM\:SS) |
| `INTERVAL`  | 두 날짜/시간 간의 기간을 표현                         |

#### 기타 유용한 타입
| 타입        | 설명                                  |
| --------- | ----------------------------------- |
| `BOOLEAN` | 참/거짓 값을 표현 (`true`, `false`)        |
| `JSON`    | JSON 형식의 데이터 저장                     |
| `JSONB`   | 이진 형태의 JSON. 빠른 검색 및 인덱싱 가능         |
| `UUID`    | 범용 고유 식별자. 충돌 없는 유일 ID 생성에 사용       |
| `ARRAY`   | 배열 형태의 데이터 저장. 여러 값을 한 컬럼에 저장할 때 사용 |

<br/>

## 2. 제약조건
테이블의 데이터 무결성을 보장하기 위해 다양한 제약조건을 설정할 수 있다.
```sql
CREATE TABLE Sales.Orders (
  order_id INT PRIMARY KET,
  member_id INT NOT NULL, 
  order_date DATE DEFALUE (CURRENT_DATE()), 
  total_amount DECIMAL(10, 2),
  status ENUM('pending', 'completed', 'cancelled'),
);
```
이러한 제약조건들의 의미는:
- NOT NULL: 필수 입력 필드
- CHECK: 데이터 유효성 검사
- FOREIGN KEY: 다른 테이블과의 관계 설정
- DEFAULT: 기본값 설정

<br/>

### 생각 보다 많이 쓰이는 제약 조건들 모음

```sql
-- 도서 목록 테이블
CREATE TABLE Books (
  book_id SERIAL PRIMARY KEY, -- 책 고유 번호
  title VARCHAR(100) -- 책 제목
);

-- 대출 기록 테이블
CREATE TABLE Loans (
  loan_id SERIAL PRIMARY KEY,
  book_id INT REFERENCES Books(book_id), -- 왜래키: 실제 존재하는 책만 대출
  borrower_name VARCHAR(100),
  loan_date DATE
);

-- 회원 테이블
CREATE TABLE Members (
  member_id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  birth_date DATE CHECK (birth_date > '1900-01-01'),
  join_date DATE DEFAULT CURRENT_DATE,
  status VARCHAR(20) CHECK (status IN ('active', 'suspended', 'expired'))
);

-- 도서 테이블
CREATE TABLE Books (
  book_id SERIAL PRIMARY KEY,
  isbn VARCHAR(13) UNIQUE NOT NULL,
  title VARCHAR(200) NOT NULL,
  price DECIMAL(10, 2) CHECK (price >= 0),
  stock_quantity INT DEFAULT 1 CHECK (stock_quantity >= 0)
);

-- 대출 테이블
CREATE TABLE Loans (
    loan_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Members(member_id) ON DELETE RESTRICT, -- Members 테이블 참조, 삭제 제한
    book_id INT REFERENCES Books(book_id) ON DELETE CASCADE, -- Books 테이블 참조, 삭제 시 대출 기록 함께 삭제
    loan_date DATE DEFAULT CURRENT_DATE, 
    due_date DATE,
    return_date DATE, 
    CONSTRAINT valid_dates CHECK ( 
        return_date IS NULL OR -- 반납일은 NULL 이거나
        (
            return_date >= loan_date -- 대출일보다 이후이고
            AND return_date <= CURRENT_DATE -- 현재 날짜보다 이전이어야 함
        )
    )
);

```

<br/>

## 3. 인덱스
테이블의 검색 성능을 향상시키기 위해 인덱스를 생성
```sql
-- 주소 이름으로 빠른 검색을 위한 인덱스
CREATE INDEX idx_address_id
ON customer.address(address_id);
```
인덱스가 없다면 데이터베이스는 테이블의 모든 행을 하나씩 검색해야 함.  
➜ 이를 FULL TABLE SCAN이라고 함.
하지만 인덱스가 있으면 원하는 데이터를 빠르게 찾을 수 있다.

<br/>
### 단점
- 인덱스는 추가 저장 공간을 사용
- 데이터가 추가, 수정, 삭제될 때마다 인덱스도 함계 업데이트해야 하므로 성능 저하가 발생
- 테이블에 데이터가 적다면 인덱스가 오히려 성능을 저하

<br/>

### 생성팁
- 자주 검색되는 컬럼
- 데이터의 중복이 적은 컬럼
- 테이블의 데이터가 충분히 많은 경우

<br/>

## 4. 파티셔닝
대용량 테이블의 경우, 데이터를 더 효율적으로 관리하기 위해 파티셔닝을 사용
```sql
CREATE TABLE Sales.Orders1 (
    order_id INT,
    member_id INT NOT NULL,
    order_date DATE DEFAULT (CURRENT_DATE()),
    total_amount DECIMAL(10,2),
    status ENUM('pending', 'completed', 'cancelled'),
    PRIMARY KEY (order_date, order_id)
)
PARTITION BY RANGE (YEAR(order_date)) (
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION p2025 VALUES LESS THAN (2026),
    PARTITION p_future VALUES LESS THAN MAXVALUE
);
```
- MySQL에서 파티셔닝을 사용할 때는 파티셔닝 키가 반드시 PRIMARY KEY의 일부여야 함
- PARTITION 구문은 특정 연도의 데이터를 저장할 공간을 만듭니다.
  - p2023, p2024, p2025, p_futre: 2026년 이후의 모든 주문 데이터
 
이렇게 파티셔닝을 하면 다음과 같은 이점이 존재
1. 검색 성능 향상: 2024년의 주문만 찾고 싶다면, 다른 연도의 데이터는 검색하지 않아도 됨.
2. 관리 용이성: 오래된 데이터를 쉽게 아카이브하거나 삭제할 수 있다.
3. 백업 효율성: 특정 기간의 데이터만 선택적으로 백업



