import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("worldometer_data.csv")

print(df.shape)
print(df.head())

df.plot(x="Population", y="TotalCases", kind="scatter", figsize=(8,5), title="Casos confirmados x População")
plt.xlabel("População")
plt.ylabel("Casos Confirmados")
plt.show()

top10_deaths = df.sort_values("TotalDeaths", ascending=False).head(10)
top10_deaths.plot(x="Country/Region", y="TotalDeaths", kind="bar", figsize=(10,5), title="Top 10 países - Mortes")
plt.show()
