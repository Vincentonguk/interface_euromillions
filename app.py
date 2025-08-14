import streamlit as st
import pandas as pd
from datetime import datetime
from gerador_loterias import GAMES, generate_lines, lines_to_dataframe

st.set_page_config(page_title="Lottery Number Generator (UK)", page_icon="🎟️", layout="centered")

st.title("🎟️ Lottery Number Generator — EuroMillions, Lotto, Set For Life")
st.caption("Educational project: generate random combinations for the main UK lottery games.")

with st.sidebar:
    st.header("Settings")
    game_key = st.selectbox(
        "Game",
        options=list(GAMES.keys()),
        format_func=lambda k: GAMES[k].name
    )
    qnt = st.number_input("Number of lines", min_value=1, max_value=50, value=5, step=1)
    avoid_duplicates = st.toggle("Avoid duplicate lines in batch", value=True)
    seed_opt = st.text_input("Seed (optional, for reproducible results)", value="")
    seed = seed_opt.strip() if seed_opt.strip() else None
    generate = st.button("Generate combinations", type="primary", use_container_width=True)

if generate:
    lines = generate_lines(game_key, n_lines=int(qnt), unique_lines=avoid_duplicates, seed=seed)
    spec = GAMES[game_key]
    df = lines_to_dataframe(lines, spec)
    st.subheader(f"Results — {spec.name}")
    st.dataframe(df, use_container_width=True)

    # Copyable text
    as_text = "\n".join([", ".join(map(str, row)) for row in df.values.tolist()])
    st.code(as_text, language="text")

    # CSV download
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"picks_{game_key}_{ts}.csv"
    st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=filename,
        mime="text/csv",
        use_container_width=True
    )

    st.info("⚠️ Disclaimer: This is for educational/entertainment purposes only. Gambling involves risks. Play responsibly.")
else:
    st.write("Choose a **game** from the sidebar, set the **number of lines**, and click **Generate combinations**.")

with st.expander("ℹ️ About the games"):
    st.markdown(
        """
        **EuroMillions**: 5 numbers (1–50) + 2 Lucky Stars (1–12)  
        **Lotto (UK)**: 6 numbers (1–59)  
        **Set For Life**: 5 numbers (1–47) + 1 Life Ball (1–10)
        """
    )