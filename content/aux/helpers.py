## PLOTS

import matplotlib.pyplot as plt
 
MEDIA = ["television", "paid_search", "social_media", "trade"]
 
df[MEDIA].plot(subplots=True, figsize=(11, 6), title="Weekly spend by channel")


## EXPLAIN OPTIMIZATION

import pandas as pd
from sklearn.linear_model import LinearRegression

MEDIA = ["television", "paid_search", "social_media", "trade"]

df = pd.read_csv("spain_allegra_weekly.csv").dropna()

model = LinearRegression()
model.fit(df[MEDIA], df["volume"])

roi = dict(zip(MEDIA, model.coef_))
for channel, value in roi.items():
    print(f"{channel}: ROI = {value:.2f}")

def optimize_spend(total_budget):
    best = max(roi, key=roi.get)
    plan = {channel: 0 for channel in MEDIA}
    plan[best] = total_budget
    return plan


if __name__ == "__main__":
    print("Recommended budget split for a 1,000,000 budget:")
    print(f"{optimize_spend(1_000_000)}")
 