import streamlit as st
import pandas as pd

st.title("App Streamlit")

st.header("Imóveis Recife")
st.write("Previsão de Preços")

st.subheader("Entrada de Dados")

nome = st.text_input("Digite seu nome")
idade = st.number_input("Digite dua idade", min_value=0, max_value=120, value=25)
bairo = st.selectbox(
    "Escolha um bairro",
    ["Boa viagem", "Casa Amarela", "Madalena"]
)
area = st.slider("Informe a área", 20, 200, 70)

st.subheader("Dados informados")

st.write("Nome:", nome)
st.write("Idade:", idade)

if st.button("Calcular Preço Estimado"):
    preco = area * 1000
    st.success(f"Preço estimado: R$ {preco}")

dados = {
    "Bairro": ["Boa Viagem", "Casa Amarela", "Madalena"], 
    "Área": [100,70,50],
    "Preço": [1000000, 50000, 3000]
}

df = pd.DataFrame(dados)

st.dataframe(df)

st.bar_chart(df.set_index("Bairro")["Preço"])