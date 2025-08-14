import streamlit as st
import pandas as pd
from datetime import datetime
from gerador_loterias import GAMES, generate_lines, lines_to_dataframe

st.set_page_config(page_title="Gerador de Loterias (UK)", page_icon="🎟️", layout="centered")

st.title("🎟️ Gerador de Números — EuroMillions, Lotto, Set For Life")
st.caption("Projeto didático: gere combinações aleatórias para os principais jogos do Reino Unido.")

with st.sidebar:
    st.header("Configurações")
    game_key = st.selectbox(
        "Jogo",
        options=list(GAMES.keys()),
        format_func=lambda k: GAMES[k].name
    )
    qnt = st.number_input("Quantidade de linhas", min_value=1, max_value=50, value=5, step=1)
    evitar_linhas_duplicadas = st.toggle("Evitar linhas duplicadas no lote", value=True)
    seed_opt = st.text_input("Semente (opcional, para reproduzir resultados)", value="")
    seed = seed_opt.strip() if seed_opt.strip() else None
    gerar = st.button("Gerar combinações", type="primary", use_container_width=True)

if gerar:
    lines = generate_lines(game_key, n_lines=int(qnt), unique_lines=evitar_linhas_duplicadas, seed=seed)
    spec = GAMES[game_key]
    df = lines_to_dataframe(lines, spec)
    st.subheader(f"Resultados — {spec.name}")
    st.dataframe(df, use_container_width=True)

    # Texto simples para copiar
    as_text = "\n".join([", ".join(map(str, row)) for row in df.values.tolist()])
    st.code(as_text, language="text")

    # Download CSV
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"picks_{game_key}_{ts}.csv"
    st.download_button(
        label="Baixar CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=filename,
        mime="text/csv",
        use_container_width=True
    )

    st.info("⚠️ Aviso: Isto é apenas para fins educacionais/diversão. Jogos de azar envolvem riscos. Jogue com responsabilidade.")
else:
    st.write("Escolha um **jogo** na barra lateral, ajuste a **quantidade de linhas** e clique em **Gerar combinações**.")

with st.expander("ℹ️ Sobre os jogos"):
    st.markdown(
        """
        **EuroMillions**: 5 números (1–50) + 2 Lucky Stars (1–12)  
        **Lotto (UK)**: 6 números (1–59)  
        **Set For Life**: 5 números (1–47) + 1 Life Ball (1–10)
        """
    )