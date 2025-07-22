import streamlit as st
import pandas as pd
import random

st.title("Smart EuroMillions Generator")

num_combinations = st.slider("How many combinations would you like to generate?", 1, 10, 1)

results = []
for _ in range(num_combinations):
    numbers = sorted(random.sample(range(1, 51), 5))
    stars = sorted(random.sample(range(1, 13), 2))
    results.append({"Numbers": numbers, "Stars": stars})

df = pd.DataFrame(results)

st.table(df)

csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="euromillions_combinations.csv",
    mime="text/csv",
)
