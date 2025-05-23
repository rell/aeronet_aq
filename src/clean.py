import pandas as pd

desired_cols = ["sitename", "Latitude", "Longitude"]
df = pd.read_csv("./station_270_updates_Feb_11_2025_updated.csv", encoding="latin-1")
df2 = pd.read_csv("./stations_AERONET_07262024.csv", encoding="latin-1")
df3 = pd.read_csv("./stations_OpenAQ_05082025.csv", encoding="latin-1")
df = pd.concat([df[desired_cols], df2[desired_cols], df3[desired_cols]], axis=0)

for col in df.columns:
    df[col] = df[col].astype(str).replace(",", ";")

df.to_csv("out.csv", index=False)
