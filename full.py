import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("full_grouped.csv")

print(df.shape)
print(df.head())

# Evolução de casos globais
global_cases = df.groupby("Date")["Confirmed"].sum()
global_cases.plot(figsize=(10,5), title="Evolução Global de Casos Confirmados")
plt.ylabel("Casos")
plt.show()

# Comparação de alguns países
countries = ["Brazil", "India", "USA"]
for c in countries:
    df_country = df[df["Country/Region"] == c].groupby("Date")["Confirmed"].sum()
    plt.plot(df_country.index, df_country.values, label=c)

plt.legend()
plt.title("Comparação da evolução - Brasil, Índia e EUA")
plt.ylabel("Casos Confirmados")
plt.show()
