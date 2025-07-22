import streamlit as st
import random
import pandas as pd

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

st.title("Smart EuroMillions Generator")
qty = st.slider("How many combinations would you like to generate?", 1, 50, 10)

if st.button("Generate Combinations"):
    combinations = generate_combinations(qty)
    df = pd.DataFrame(combinations)
    st.dataframe(df)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "euromillions_combinations.csv", "text/csv")
