
import streamlit as st
import random
import pandas as pd

# Dados pré-processados
top_numeros = [34, 25, 42, 29, 17, 48, 37, 10, 19, 12, 39, 5, 49, 7, 16, 20, 44, 47, 50, 9]
top_estrelas = [5, 8, 1, 4, 9]

# Função para gerar combinações
def gerar_combinacoes(qtd=10):
    return [
        {
            'Numeros': sorted(random.sample(top_numeros, 5)),
            'Estrelas': sorted(random.sample(top_estrelas, 2))
        }
        for _ in range(qtd)
    ]

# Interface Streamlit
st.title("Gerador Inteligente EuroMillions")
qtd = st.slider("Quantas combinações deseja gerar?", 1, 50, 10)

if st.button("Gerar Combinações"):
    combinacoes = gerar_combinacoes(qtd)
    df = pd.DataFrame(combinacoes)
    st.dataframe(df)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Baixar CSV", csv, "combinacoes_euromillions.csv", "text/csv")
