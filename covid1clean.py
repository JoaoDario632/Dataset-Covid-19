import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid_19_clean_complete.csv")

print(df.shape)
print(df.head())

print(df.describe())

country = "Brazil"
df_brazil = df[df["Country/Region"] == country]
df_brazil.groupby("Date")["Confirmed"].sum().plot(figsize=(10,5), title=f"Evolução COVID-19 - {country}")
plt.ylabel("Casos confirmados")
plt.show()
