import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------- Configuração -------------------
st.set_page_config(page_title="Dashboard COVID-19", page_icon="🦠", layout="wide")

# ------------------- Carregar dados -------------------
day_wise = pd.read_csv("day_wise.csv")
country_wise_latest = pd.read_csv("country_wise_latest.csv")
worldometer_data = pd.read_csv("worldometer_data.csv")
usa_county_wise = pd.read_csv("usa_county_wise.csv")
full_grouped = pd.read_csv("full_grouped.csv")
covid_19_clean_complete = pd.read_csv("covid_19_clean_complete.csv")

# Criar colunas auxiliares
country_wise_latest["Fatality Rate"] = (country_wise_latest["Deaths"] / country_wise_latest["Confirmed"]) * 100

# ------------------- Menu Lateral -------------------
st.sidebar.title("📌 Navegação")
page = st.sidebar.radio("Escolha uma seção:", [
    "🏠 Página Inicial",
    "🌐 Casos Globais",
    "🌍 Países",
    "🇺🇸 Estados Unidos",
    "📖 Insights e Conclusões"
])

# ------------------- Página Inicial -------------------
if page == "🏠 Página Inicial":
    st.title("🦠 Dashboard Interativo - COVID-19")
    st.markdown("""
    Bem-vindo ao **Dashboard Interativo da COVID-19**!  
    Aqui você encontrará diferentes perspectivas sobre a pandemia com os gráficos interativos.

    ### 📝 Dados:
    Os dados utilizados para construir esse dashboard foram obtidos do [Kaggle](https://www.kaggle.com/datasets/imdevskp/corona-virus-report).
    Eles incluem informações diárias sobre casos confirmados, mortes e recuperações em nível global, nacional e estadual (EUA).
    Os datasets foram atualizados pela última vez em meados de 2020, então os dados refletem o estado da pandemia até essa data.

    ### 📑 Estrutura:
    - **🌐 Casos Globais**: visão do mundo (casos acumulados, novos casos, mapa).  
    - **🌍 Países**: evolução em países selecionados, rankings e letalidade.  
    - **🇺🇸 Estados Unidos**: análise dos estados americanos.  
    - **📖 Sumário**: principais conclusões e insights.  
                
    ### 📚 Referências desses dados Kaggle:
    - Fonte de Dados - [COVID-19](https://github.com/CSSEGISandData/COVID-19)
    - Metodologia coletânea - [covid_19_jhu_data_web_scrap_and_cleaning](https://github.com/imdevskp/covid_19_jhu_data_web_scrap_and_cleaning)
                
    ### 🚀 Navegação:
    Use o menu lateral ⬅️ para navegar pelas seções.
    """)

# ------------------- Casos Globais -------------------
elif page == "🌐 Casos Globais":
    st.header("🌐 Casos Globais")

    st.subheader("Casos Totais vs População (escala log)")
    fig1 = px.scatter(worldometer_data, x="Population", y="TotalCases",
                      size="TotalCases", color="Continent",
                      hover_name="Country/Region", log_x=True, log_y=True)
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Casos Confirmados Acumulados no Mundo")
    fig2 = px.line(day_wise, x="Date", y="Confirmed")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Novos Casos Globais por Dia")
    fig3 = px.line(day_wise, x="Date", y="New cases")
    st.plotly_chart(fig3, use_container_width=True)

# ------------------- Países -------------------
elif page == "🌍 Países":
    st.header("🌍 Análise por Países")

    st.subheader("Top 10 Países por Casos Totais")
    top10_cases = country_wise_latest.sort_values("Confirmed", ascending=False).head(10)
    fig4 = px.bar(top10_cases, x="Country/Region", y="Confirmed")
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("Top 10 Países por Taxa de Letalidade (%)")
    top10_fatality = country_wise_latest.sort_values("Fatality Rate", ascending=False).head(10)
    fig5 = px.bar(top10_fatality, x="Country/Region", y="Fatality Rate")
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("Evolução dos Casos Confirmados em Países Selecionados")
    countries = st.multiselect("Selecione os países:", ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burma", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Brazzaville)", "Congo (Kinshasa)", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Diamond Princess", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "MS Zaandam", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Mauritania", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan*", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Trinidad and Tobago", "Tunisia", "Turkey", "US", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "West Bank and Gaza", "Western Sahara", "Yemen", "Zambia", "Zimbabwe"], default=["Brazil","US", "Russia", "United Kingdom"])
    df_countries = full_grouped[full_grouped["Country/Region"].isin(countries)]
    fig6 = px.line(df_countries, x="Date", y="Confirmed", color="Country/Region")
    st.plotly_chart(fig6, use_container_width=True)

    st.subheader("Novos Casos por Dia em Países Selecionados")
    df_new_cases = df_countries.groupby(["Date", "Country/Region"])["New cases"].sum().reset_index()
    fig7 = px.line(df_new_cases, x="Date", y="New cases", color="Country/Region")
    st.plotly_chart(fig7, use_container_width=True)

# ------------------- EUA -------------------
elif page == "🇺🇸 Estados Unidos":
    st.header("🇺🇸 Estados Unidos - Casos por Estado")

    st.subheader("Top 15 Estados por Casos Confirmados")
    usa_grouped = usa_county_wise.groupby("Province_State")["Confirmed"].max().sort_values(ascending=False).head(15)
    fig8 = px.bar(usa_grouped, x=usa_grouped.index, y=usa_grouped.values,
                  labels={"x": "Estado", "y": "Casos Confirmados"})
    st.plotly_chart(fig8, use_container_width=True)

# ------------------- Sumário -------------------
elif page == "📖 Insights e Conclusões":
    st.header("📖 Insights e Conclusões")
    st.markdown("""
    ### ✅ Principais Insights
    - 🌐 **Casos globais** cresceram exponencialmente no início, mas depois estabilizaram em alguns países.  
    - 🌍 **Brasil, Índia e EUA** figuram entre os países mais afetados em número absoluto.  
    - ⚠️ **Taxa de letalidade** varia muito entre países, refletindo infraestrutura de saúde e testagem.  
    - 🇺🇸 Nos **EUA**, alguns estados concentram a maior parte dos casos confirmados.  
    - 📉 A análise de **novos casos diários** mostra picos e quedas, indicando ondas da pandemia.
    - 🗺️ O mapa interativo destaca a distribuição desigual dos casos globalmente.
    - 📊 Gráficos interativos permitem explorar tendências e comparar países/estados.

    ### 📌 Conclusão
    O painel evidencia que a pandemia da COVID-19 se disseminou de maneira desigual entre países e regiões, revelando diferenças significativas na evolução dos casos, na taxa de letalidade e na capacidade de resposta de cada localidade.
    As visualizações interativas permitem identificar padrões globais e regionais, comparar tendências e compreender melhor os fatores que influenciaram a propagação e os impactos da doença.
    
    ➡️ Esse tipo de análise comparativa e regionalizada é essencial para subsidiar decisões em saúde pública, orientar estratégias de contenção e auxiliar na preparação para futuros cenários epidemiológicos.
    
    """) 