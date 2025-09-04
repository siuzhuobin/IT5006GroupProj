import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd 
import seaborn as sns 
from x105Shared import load_data 

diabetes, var_dict = load_data()
int_columns = var_dict["int_columns"]
string_columns = var_dict["string_columns"]
ordinal_orders = var_dict["ordinal_orders"]


ordinal_columns = int_columns
categorical_columns = [c for c in string_columns if not c in ["age","encounter_id","patient_nbr"]]

st.title('Box plots')

bpX = st.selectbox(label='Plot x', options=int_columns, index=0, key='bpX')
bpY = st.selectbox(label='Plot y', options=['None'] + categorical_columns, index = 0, key = 'bpY')

plt.clf()
plt.figure()
if (bpY == 'None'):
    ax = sns.boxplot(data=diabetes, x=bpX)
else:
    ax = sns.boxplot(data=diabetes, x=bpX, y=bpY)
fig = ax.get_figure()
st.pyplot(fig)

st.title('Histograms')

htX = st.selectbox(label='Plot x', options=int_columns, index=0, key='htX')
htBin = st.selectbox(label='Bins', options = ['Auto'] + [str(x) for x in range(4,9)], index = 0, key='htBin')

plt.clf()
plt.figure()
if (htBin == 'Auto'):
    ax = sns.histplot(data=diabetes, x=htX)
else:
    ax = sns.histplot(data=diabetes, x=htX, bins = int(htBin))
fig = ax.get_figure()
st.pyplot(fig)
st.caption('Data counts')
st.dataframe(diabetes[htX].value_counts())

if False:
    plt.clf()
    plt.figure()
    st.title('KDE plot')
    kdX = st.selectbox(label='Plot x', options=int_columns, index=0, key='kdX')
    kdHue = st.selectbox(label='Hue', options=['None'] + categorical_columns, index = 0, key = 'kdHue')

    if kdHue == 'None':
        ax = sns.kdeplot(data=diabetes,x=kdX)
    else:
        ax = sns.kdeplot(data=diabetes,x=kdX, hue=kdHue)
    fig = ax.get_figure()
    st.pyplot(fig)


st.title('Counts')
plt.clf()
plt.figure()

cbX = st.selectbox(label='Plot x', options=categorical_columns, index=0, key='cbX')
cbHue = st.selectbox(label='Hue', options=['None'] + categorical_columns, index = 0, key = 'cbHue')

cbHue=None if cbHue == 'None' else cbHue
ax = sns.countplot(data=diabetes,x=cbX, hue=cbHue)
fig = ax.get_figure()
st.pyplot(fig)
