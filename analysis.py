import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\hp\Downloads\archive (2)\city_day.csv")

#-----------------------
# Filling missing values
#-----------------------
gase = ["NO", "NO2", "NOx", "NH3", "CO", "SO2", "O3"]
air_quality = ["Benzene", "Toluene", "Xylene"]

median_cols = ["PM2.5", "PM10", "AQI"] + gase + air_quality
df[median_cols] = df[median_cols].fillna(df[median_cols].median())

df["AQI_Bucket"] = df["AQI_Bucket"].fillna(df["AQI_Bucket"].mode()[0])

#---------------------
# IQR Outlier Handling
#---------------------
numeric_col = median_cols

for col in numeric_col:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR

    median_val = df[col].median()
    
    df[col] = np.where((df[col] < lower) | (df[col] > upper), median_val, df[col])

#---------------------
# Convert date to Year
#---------------------
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Year"] = df["Date"].dt.year
df = df.dropna(subset=["Year"])

#--------------------------------
#Top 10 Most Polluted Cities (AQI)
#--------------------------------
high_aqi = df.groupby("City")["AQI"].mean().sort_values(ascending=False)
most_tencity = high_aqi.head(10)

plt.figure(figsize=(10,6))
plt.bar(most_tencity.index, most_tencity.values, color="blue", label="Most Ten AQI City")
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Most Polluted Cities (AQI)")
plt.xlabel("City")
plt.ylabel("AQI")
plt.legend()
plt.tight_layout()

plt.show()

#--------------------
#Year Wise AQI Trends
#--------------------
year_wise = df.groupby("Year")["AQI"].mean()
plt.figure(figsize=(10,6))
plt.plot(year_wise.index, year_wise.values, marker="o", color="red", label="Year Wise AQI")
plt.title("YEAR WISE AQI TRENDS")
plt.xlabel("YEAR")
plt.ylabel("AQI")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()

#---------------------
#CITY WISE HEATMAP AQI
#---------------------
pivot_city = df.pivot_table(
    index="City",
    columns="Year",
    values="AQI",
    aggfunc="mean"
)
plt.figure(figsize=(14,10))
plt.imshow(pivot_city, aspect="auto")
plt.colorbar(label="Average AQI")
plt.xticks(range(len(pivot_city.columns)), pivot_city.columns)
plt.yticks(range(len(pivot_city.index)), pivot_city.index)
plt.title("CITY WISE HEATMAP AQI")
plt.xlabel("YERA")
plt.ylabel("CITY")
plt.tight_layout()
plt.show()
