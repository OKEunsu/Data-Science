from geopy.distance import geodesic
from tqdm import tqdm

def find_nearby_stores(email_df, store_df, radius_km=1):
nearby_store_counts = []

for index, row in email_df.iterrows():
    user_location = (row['위도'], row['경도'])
    nearby_count = 0

    for idx, store_row in store_df.iterrows():
        store_location = (store_row['위도'], store_row['경도'])
        distance = geodesic(user_location, store_location).kilometers

        if distance <= radius_km:
            nearby_count += 1

    nearby_store_counts.append(nearby_count)

return nearby_store_counts

# seoul_login 데이터프레임에 '화면 가게수' 열 추가
seoul_login['화면 가게수'] = 0  # 초기화
for idx, row in tqdm(seoul_login.iterrows(), total=seoul_login.shape[0], desc="Processing gyeonggi"):
    row_df = row.to_frame().T  # Series를 DataFrame으로 변환
    seoul_login.at[idx, '화면 가게수'] = find_nearby_stores(row_df, seoul_store)
