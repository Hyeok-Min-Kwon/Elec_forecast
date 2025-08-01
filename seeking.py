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