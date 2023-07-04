import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Carregar os dados
url = 'postgres://imdqzcun:CfF9UzqSW9Xtt21xOtICzar2gilw4A7M@silly.db.elephantsql.com/imdqzcun'
df = pd.read_csv(url)

# Visão geral do DataFrame usando Streamlit
st.title('Análise Exploratória de Dados')
st.subheader('Visão geral dos dados')
st.write(df.head())

# Informações gerais sobre os dados
st.subheader('Informações gerais sobre os dados')
st.write(df.info())

# Estatísticas descritivas
st.subheader('Estatísticas descritivas dos dados')
st.write(df.describe())

# Verificar valores ausentes
st.subheader('Valores ausentes')
st.write(df.isnull().sum())

# Análise exploratória de algumas colunas selecionadas usando gráficos
st.subheader('Análise exploratória de algumas colunas')

# Gráfico de contagem para uma coluna categórica
coluna_categorica = st.selectbox('Selecione uma coluna categórica', df.columns[df.dtypes == 'object'])
fig_bar = plt.figure(figsize=(8, 6))
sns.countplot(x=coluna_categorica, data=df)
plt.xticks(rotation=45)
st.pyplot(fig_bar)

# Gráfico de distribuição para uma coluna numérica
coluna_numerica = st.selectbox('Selecione uma coluna numérica', df.columns[df.dtypes != 'object'])
fig_dist = plt.figure(figsize=(8, 6))
sns.histplot(df[coluna_numerica], kde=True)
st.pyplot(fig_dist)

# Gráfico de dispersão entre duas colunas numéricas
coluna_numerica_x = st.selectbox('Selecione uma coluna numérica para o eixo x', df.columns[df.dtypes != 'object'])
coluna_numerica_y = st.selectbox('Selecione uma coluna numérica para o eixo y', df.columns[df.dtypes != 'object'])
fig_scatter = plt.figure(figsize=(8, 6))
sns.scatterplot(x=coluna_numerica_x, y=coluna_numerica_y, data=df)
st.pyplot(fig_scatter)
