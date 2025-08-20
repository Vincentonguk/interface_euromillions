import streamlit as st
import random

st.set_page_config(page_title="Gerador de Loterias", layout="centered")

st.title("💰 Gerador de Números da Sorte")
st.markdown("Escolha um jogo abaixo para gerar combinações aleatórias e analisar estatísticas.")

# --- Funções para cada jogo ---

def gerar_euromillions():
    numeros = random.sample(range(1, 51), 5)
    estrelas = random.sample(range(1, 13), 2)
    return sorted(numeros), sorted(estrelas)

def gerar_lotto():
    numeros = random.sample(range(1, 60), 6)
    return sorted(numeros)

def gerar_set_for_life():
    numeros = random.sample(range(1, 48), 5)
    life_ball = random.randint(1, 10)
    return sorted(numeros), life_ball

# --- Seletor de jogo ---
jogo = st.selectbox("🎲 Selecione o jogo:", ["EuroMillions", "Lotto", "Set For Life"])

# --- Interface por jogo ---
if jogo == "EuroMillions":
    st.subheader("🔵 EuroMillions")
    if st.button("Gerar Combinação"):
        numeros, estrelas = gerar_euromillions()
        st.success(f"Números: {numeros}")
        st.info(f"Estrelas: {estrelas}")

elif jogo == "Lotto":
    st.subheader("🟢 Lotto (UK)")
    if st.button("Gerar Combinação"):
        numeros = gerar_lotto()
        st.success(f"Números: {numeros}")

elif jogo == "Set For Life":
    st.subheader("🟡 Set For Life")
    if st.button("Gerar Combinação"):
        numeros, life_ball = gerar_set_for_life()
        st.success(f"Números: {numeros}")
        st.info(f"Life Ball: {life_ball}")

# --- Rodapé ---
st.markdown("---")
st.caption("🎯 Este app é apenas para fins de entretenimento e análise. Boa sorte!")
