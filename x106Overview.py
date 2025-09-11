import streamlit as st 
import pandas as pd 
from x106Shared import load_data

@st.cache_data
def basic_analysis():
    X, y, df = load_data()
    st.header("Data Overview and Quality Assessment")
    st.write(f"Shape: {df.shape}")
    st.write(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")

    st.write("\nData Types")
    st.write(df.dtypes.value_counts())

    st.write("\nMissing Values")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df) * 100).round(1)
    missing_df = pd.DataFrame({
        'Missing Count': missing,
        'Missing Percentage (%)': missing_pct
    }).sort_values('Missing Count', ascending=False)

    st.write(missing_df[missing_df['Missing Count'] > 0])

basic_analysis()