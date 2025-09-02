import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd 
import seaborn as sns 

diabetes = pd.read_csv("clean_diabetes.csv")
ax = sns.countplot( data=diabetes, x='race', hue='gender')
fig = ax.get_figure()

st.pyplot(fig)