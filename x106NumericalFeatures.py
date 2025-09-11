import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from x106Shared import load_data


@st.cache_data
def numeric_feature_static_items():
    X, y, df = load_data()
    st.header("Statistical Properties of Numerical Features")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    st.write(f"Numerical features: {len(numeric_cols)}")
    st.write(f"Features: {' '.join(numeric_cols)}")

    # Basic statistics
    st.subheader("Descriptive Statistics")
    stats = df[numeric_cols].describe()
    stats_T = stats.T
    st.dataframe(stats_T.round(2))

    
    return X, y, df



X, y, df = numeric_feature_static_items()
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

plt.clf()
plt.figure()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))


st.subheader('Distribution Visualization')
cbX = st.selectbox(label='Numerical feature', options=numeric_cols, index=0, key='cbX')

col = cbX
df[col].hist(bins=30,  alpha=0.7, color='skyblue', ax = ax1)
ax1.set_title(f'{col} distribution')
ax1.set_xlabel(col)

crosstab = pd.crosstab(df[col], df['readmitted'], normalize='index') * 100

# Draw stacked bar chart
crosstab.plot(kind='bar', stacked=True, ax=ax2,
                color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
ax2.set_title(f'{col} vs Readmission Status')
ax2.set_ylabel('Percentage (%)')
ax2.legend(title='Readmission Status')
ax2.tick_params(axis='x', rotation=45)
st.pyplot(fig)







    
