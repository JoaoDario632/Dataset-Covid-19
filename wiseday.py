import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("day_wise.csv")

print(df.shape)
print(df.head())
print(df.describe())

df.plot(x="Date", y="Confirmed", figsize=(10,5), title="Casos Confirmados Globais")
plt.ylabel("Casos")
plt.show()
