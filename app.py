import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

st.title("🏥 Healthcare Resource Prioritization Dashboard")

file = "Healthcare_TOPSIS_Ranked_Fixed.xlsx"

if os.path.exists(file):
    df = pd.read_excel(file)
else:
    st.error("Excel file not found")
    st.stop()

df["Priority Index"] = 1 - df["TOPSIS Score"]
df["Priority Rank"] = df["Priority Index"].rank(ascending=False).astype(int)

df = df.sort_values("Priority Rank")

st.subheader("Top Priority States")
st.dataframe(df[["Priority Rank","State","Priority Index","TOPSIS Score"]])

st.subheader("Priority Chart")
chart = df.set_index("State")["Priority Index"]
st.bar_chart(chart)

st.success("Higher Priority Index = Higher Healthcare Need")
