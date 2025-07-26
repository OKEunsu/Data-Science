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

## 주요 데이터 타입, 용도
### 숫자 타입
| 타입             | 설명                                       |
| -------------- | ---------------------------------------- |
| `SERIAL`       | 자동 증가하는 정수 (1, 2, 3, ...)                |
| `INT`          | 일반 정수 (-2,147,483,648 \~ +2,147,483,647) |
| `SMALLINT`     | 작은 범위의 정수 (-32,768 \~ +32,767)           |
| `DECIMAL(p,s)` | 정확한 소수. `p`: 전체 자릿수, `s`: 소수점 이하 자릿수     |
| `FLOAT`        | 부동 소수점. 큰 범위 표현 가능하나 정확도는 떨어질 수 있음       |

### 문자열 타입
| 타입           | 설명                        |
| ------------ | ------------------------- |
| `CHAR(n)`    | 고정 길이 문자열. 남은 공간은 공백으로 채움 |
| `VARCHAR(n)` | 가변 길이 문자열. 최대 n자까지 저장 가능  |
| `TEXT`       | 길이 제한이 없는 긴 텍스트 저장에 적합    |

### 시간 관련 타입
| 타입          | 설명                                        |
| ----------- | ----------------------------------------- |
| `DATE`      | 날짜만 저장 (형식: YYYY-MM-DD)                   |
| `TIME`      | 시간만 저장 (형식: HH\:MM\:SS)                   |
| `TIMESTAMP` | 날짜와 시간을 함께 저장 (형식: YYYY-MM-DD HH\:MM\:SS) |
| `INTERVAL`  | 두 날짜/시간 간의 기간을 표현                         |

### 기타 유용한 타입
| 타입        | 설명                                  |
| --------- | ----------------------------------- |
| `BOOLEAN` | 참/거짓 값을 표현 (`true`, `false`)        |
| `JSON`    | JSON 형식의 데이터 저장                     |
| `JSONB`   | 이진 형태의 JSON. 빠른 검색 및 인덱싱 가능         |
| `UUID`    | 범용 고유 식별자. 충돌 없는 유일 ID 생성에 사용       |
| `ARRAY`   | 배열 형태의 데이터 저장. 여러 값을 한 컬럼에 저장할 때 사용 |

<br/>



