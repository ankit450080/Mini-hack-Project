import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Mini hac/smart_meter_consumption.csv")

# print(df.isnull())
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df["zone"] = df["zone"].str.lower()
df["zone"] = df["zone"].str.title()
df["zone"] = df["zone"].replace({
    "Comerical": "Commercial",
    "Commerical": "Commercial",
    "Comercial": "Commercial",
    "Industiral": "Industrial",
    "Industrail": "Industrial",
    "Residental": "Residential",
    "Residntial": "Residential"
})
print(df.head())

hourly = df.groupby(["zone","hour"])["kwh_consumed"].mean().reset_index()
top3 = hourly.groupby("zone").apply(
    lambda x: x.nlargest(3,"kwh_consumed"))
print(top3)
sns.lineplot(data= hourly,
              x = "hour",
              y = "kwh_consumed",
              hue="zone")
plt.show()
monthly = df.groupby(["month", "zone"])["kwh_consumed"].mean().reset_index()
sns.lineplot(data = monthly,
         x = "month",
         y = "kwh_consumed",
         hue = "zone",
         marker = "o")
plt.show()
