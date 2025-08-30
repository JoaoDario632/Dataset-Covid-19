import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("usa_county_wise.csv")

print(df.shape)
print(df.head())

state_cases = df.groupby("Province_State")["Confirmed"].max().sort_values(ascending=False).head(10)

# Top 10 estados dos EUA
state_cases.plot(kind="bar", figsize=(10,5), title="Top 10 Estados - Casos Confirmados")
plt.ylabel("Casos")
plt.show()
