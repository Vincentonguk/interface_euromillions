import streamlit as st
import random
import pandas as pd

# Dados principais
top_numbers = [34, 25, 42, 29, 17, 48, 37, 10, 19, 12, 39, 5, 49, 7, 16, 20, 44, 47, 50, 9]
top_stars = [5, 8, 1, 4, 9]

def generate_combinations(qty=10):
    return [
        {
            'Numbers': sorted(random.sample(top_numbers, 5)),
            'Stars': sorted(random.sample(top_stars, 2))
        }
        for _ in range(qty)
    ]

# Custom CSS
st.markdown("""
    <style>
    .main {
        text-align: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stDataFrame {
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Título centralizado
st.markdown("<h1 style='text-align: center;'>🎲 Smart EuroMillions Generator 🎲</h1>", unsafe_allow_html=True)

qty = st.slider("How many combinations would you like to generate?", 1, 50, 10)

if st.button("Generate Combinations"):
    combinations = generate_combinations(qty)
    df = pd.DataFrame(combinations)
    st.markdown("### Your combinations:")
    st.dataframe(df.style.format(na_rep="-").set_table_styles(
        [{'selector': 'th', 'props': [('text-align', 'center')]}]
    ))
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="euromillions_combinations.csv",
        mime="text/csv"
    )
