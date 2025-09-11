import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

from x106Shared import load_data

@st.cache_data
def target_analysis():
    X, y, df = load_data()

    target_counts = y['readmitted'].value_counts()
    dd = pd.DataFrame(target_counts.items(), columns=["Category", "Count"]).set_index("Category")
    target_pct = y['readmitted'].value_counts(normalize=True) * 100
    dd["Percentage"] = (dd["Count"]/dd["Count"].sum()*100).apply(lambda x: f"{x: .1f}%")

    st.header("Target Variable Distribution")
    st.table(dd)

    plt.clf()
    plt.figure()

    # Visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    target_counts.plot(kind='bar', ax=ax1, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    ax1.set_title('Readmission Status Distribution')
    ax1.set_ylabel('Count')
    ax1.tick_params(axis='x', rotation=45)

    target_pct.plot(kind='pie', ax=ax2, autopct='%1.1f%%', 
                    colors=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    ax2.set_title('Readmission Status Proportions')
    ax2.set_ylabel('')
    plt.tight_layout()

    st.pyplot(fig)

target_analysis()