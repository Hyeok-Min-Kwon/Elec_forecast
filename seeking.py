import pandas as pd

train = pd.read_csv("data/train.csv", encoding="utf-8")
building_info = pd.read_csv("data/building_info.csv", encoding="utf-8")

# building_info에서 '건물번호' 컬럼 제외한 나머지 컬럼 준비
building_info_wo_number = building_info.drop(columns=["건물번호"])

# train과 building_info를 '건물번호' 기준으로 merge
merged = pd.concat(
    [
        train,
        building_info_wo_number.set_index(building_info["건물번호"])
        .reindex(train["건물번호"])
        .reset_index(drop=True),
    ],
    axis=1,
)

# 결과 확인 (예시)
print(merged.describe())

# 컬럼명을 영어로 변경
column_mapping = {
    "num_date_time": "num_date_time",
    "건물번호": "building_num",
    "일시": "datetime",
    "기온(°C)": "temperature",
    "강수량(mm)": "rainfall",
    "풍속(m/s)": "wind_speed",
    "습도(%)": "humidity",
    "일조(hr)": "sunshine_hours",
    "일사(MJ/m2)": "solar_radiation",
    "전력소비량(kWh)": "power_consumption",
    "건물유형": "building_type",
    "연면적(m2)": "total_area",
    "냉방면적(m2)": "cooling_area",
    "태양광용량(kW)": "solar_capacity",
    "ESS저장용량(kWh)": "ess_capacity",
    "PCS용량(kW)": "pcs_capacity",
}

# 컬럼명 변경
merged = merged.rename(columns=column_mapping)

# 변경된 컬럼명 확인
print("\n변경된 컬럼명:")
print(merged.columns.tolist())
print(f"\n데이터프레임 크기: {merged.shape}")
