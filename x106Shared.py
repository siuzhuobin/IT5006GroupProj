import pandas as pd 
import streamlit as st 
import os

@st.cache_data
def load_data():
    print(os.listdir("."))
    X = pd.read_csv("diabetes_features.csv")
    y = pd.read_csv("diabetes_target.csv")
    df = pd.concat([X, y], axis=1)
    return X, y, df
