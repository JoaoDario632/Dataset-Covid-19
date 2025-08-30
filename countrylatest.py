import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("country_wise_latest.csv")

print(df.shape)
print(df.head())
print(df.describe())

top10 = df.sort_values("Confirmed", ascending=False).head(10)
top10.plot(x="Country/Region", y="Confirmed", kind="bar", figsize=(10,5), title="Top 10 países - Casos Confirmados")
plt.ylabel("Casos")
plt.show()
