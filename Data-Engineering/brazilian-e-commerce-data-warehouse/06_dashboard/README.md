# 이커머스 대시보드 구성안 (경영진용)
> 목적: 경영진이 전체 매출 흐름과 전략 방향을 빠르게 파악할 수 있도록 핵심 지표와 트렌드를 시각화

## 대시보드 구조
### 1. 사이드바 (필터)
- 날짜 선택기 (월 단위)
- 지역 선택: 주(State) 또는 도시(city) 단위 필터링
- 카테고리 선택: 상품 카테고리 필터링

---
### 2. 상단 KPI 카드 (5개)
- 총 매출(Total Sales)
- 총 주문수(Total Orders)
- 구매자 수 (Total Customers)
- 평균 객단가 (AOV)
- 고객 생애 가치 (LTV)
> KPI 지표는 이전 월 대비 변화율(%)도 함께 표시

---
### 3. 경영 지표 시각화
- 매출 트렌드: 월별 매출 추이 (라인차트)
- 카테고리별 매출 분포: 누적 바차트 or 선호 카테고리 랭킹
- 결제 수단 분포 (선택): 신용카드 / 볼레토 등


---
### 4. 운영 효율성 지표
- 정시 배송률 (%)
- 평균 배송 소요시간 (일수)

- 재구매율 (%)
- 고객 평균 평점 (1~5)

---
### 5. 지역별 성과
- 브라질 주별 매출 히트맵 (지도 or Choropleth)
- 주별 AOV / 고객 수 / 리뷰 평점
- 지역별 배송 성능 (소요시간, 정시율)


---
### 6. 인사이트 & 전략 제안 & PDF 다운
> 대시보드 기반의 주요 비즈니스 인사이트를 요약하고,   
> 경영진이 실행 가능한 전략을 제안하는 섹션입니다.

#### 🔍 인사이트 요약
- 월별 매출 흐름과 전환 지점 분석
- 지역/카테고리별 성과 편차 확인
- 고객 행동 지표(LTV, AOV, 재구매율) 기반 세그먼트 구분
- 배송 효율성 및 품질 이슈 지역 파악

#### 🚀 전략 제안
- 재고/물류 효율성 강화: 배송 소요시간이 높은 지역에 물류 재배치 고려
- 지역별 전략 집중: 높은 AOV/평점 지역에 마케팅 예산 집중
- 카테고리 성장 전략: 성장률 높은 카테고리에 상품군 강화
- LTV 기반 고객 관리: 충성 고객 유지 및 업셀링 전략 도입

#### 📄 PDF 다운로드
- 인사이트 및 전략 요약 리포트를 PDF로 저장 가능
- 회의용 자료, 외부 보고용으로 활용

---
# 대시보드 화면(Streamlit)
<img width="1909" height="951" alt="image" src="https://github.com/user-attachments/assets/6e28055a-aed7-4c9c-b9f3-acc34e04b84d" />
<img width="1917" height="956" alt="image" src="https://github.com/user-attachments/assets/1f66b91f-c905-478c-80ac-0af950cc5d0d" />
<img width="1912" height="954" alt="image" src="https://github.com/user-attachments/assets/6f1414d2-d9a2-422f-8a6c-97a027a82b06" />
<img width="1910" height="838" alt="image" src="https://github.com/user-attachments/assets/75a0da13-f416-46ea-a509-7998def3c217" />
<img width="1914" height="955" alt="image" src="https://github.com/user-attachments/assets/3c66c8be-bbe9-4cf2-9a10-68fe3a5df381" />


