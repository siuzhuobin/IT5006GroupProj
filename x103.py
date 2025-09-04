import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd 
import seaborn as sns 



int_columns = ['time_in_hospital', 'num_lab_procedures', 'num_procedures', 'num_medications', 'number_outpatient', 'number_emergency', 'number_inpatient', 'number_diagnoses']
string_columns = ['encounter_id', 'patient_nbr', 'race', 'age', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id', 'diag_1', 'diag_2', 'diag_3', 'metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'glipizide', 'glyburide', 'pioglitazone', 'rosiglitazone', 'change', 'diabetesMed', 'readmitted']

drug_columns = ['metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'glipizide', 'glyburide', 'pioglitazone', 'rosiglitazone', 'insulin']

ordinal_columns = ['age','readmitted']

number_of_bins = 8

@st.cache_data
def load_and_bin_data(int_columns, string_columns, number_of_bins = 8):
# ok let's bin the numerical data
    diabetes = pd.read_csv("clean_diabetes.csv")
    # read the columns, then cast the types to simpler types
    diabetes[int_columns] = diabetes[int_columns].astype(int)
    diabetes[string_columns] = diabetes[string_columns].astype(str)

    binned_diabetes = diabetes.copy()
    
    # actually prolly no need
    ordinal_orders = {'age': ['[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', '[50-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)'],
                      'readmitted':['<30','>30','NO']}

    for ii in int_columns:
        unique_entry_count = len(diabetes[ii].unique())
        if (unique_entry_count > number_of_bins):
            cat = pd.cut(diabetes[ii], bins = number_of_bins)
            binned_diabetes['binned_' + ii] = cat
            binned_diabetes.drop(ii, axis = 1,inplace=True)

    return diabetes, binned_diabetes, ordinal_orders


diabetes, binned_diabetes, bin_categories = load_and_bin_data(int_columns, string_columns, number_of_bins)
#hm1 = st.selectbox('Column', binned_diabetes.columns, key='count_heatmap_row', index=0)
#hm2 = st.selectbox('Row', binned_diabetes.columns, key='count_heatmap_column', index=1)


hm1 = st.selectbox('Column', diabetes.columns, key='count_heatmap_column', index=2)
hm2 = st.selectbox('Row', diabetes.columns, key='count_heatmap_row', index=1)




# tt = pd.crosstab(binned_diabetes[hm1], binned_diabetes[hm2])
tt = pd.crosstab(diabetes[hm1], diabetes[hm2])
ax = sns.heatmap(tt)
fig = ax.get_figure()

st.pyplot(fig)

# ok so for like the correlation plots essentially we care about whether they're ordinal or not


ordinal_columns = int_columns
categorical_columns = string_columns

corr_diabetes = diabetes.copy()

age_categories = ['[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', '[50-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)']
corr_diabetes["age"] = pd.Categorical(corr_diabetes["age"], categories=age_categories, ordered=True)
corr_diabetes["readmitted"] = pd.Categorical(corr_diabetes["readmitted"], categories=['<30','>30','NO'], ordered=True)

corr_diabetes["age_code"] = corr_diabetes["age"].cat.codes
corr_diabetes["readmitted_code"] = corr_diabetes["age"].cat.codes

ordinal_columns = ordinal_columns + ["age_code", "readmitted_code"]
nominal_columns = categorical_columns
nominal_columns.remove("age")
nominal_columns.remove("readmitted")

#hc1 = st.selectbox('Column', ordinal_columns, key='count_heatmap_column', index=2)
#hc2 = st.selectbox('Row', ordinal_columns, key='count_heatmap_row', index=1)


corr_df = corr_diabetes[ordinal_columns]
corr = corr_df.corr(method="spearman")

ax = sns.heatmap(corr)
fig = ax.get_figure()


st.pyplot(fig)
