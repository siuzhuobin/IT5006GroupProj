import pandas as pd 
import streamlit as st 

@st.cache_data
def load_data():
# ok let's bin the numerical data

    int_columns = ['time_in_hospital', 'num_lab_procedures', 'num_procedures', 'num_medications', 'number_outpatient', 'number_emergency', 'number_inpatient', 'number_diagnoses']
    string_columns = ['encounter_id', 'patient_nbr', 'race', 'age', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id', 'diag_1', 'diag_2', 'diag_3', 'metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'glipizide', 'glyburide', 'pioglitazone', 'rosiglitazone', 'change', 'diabetesMed', 'readmitted']
#     drug_columns = ['metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'glipizide', 'glyburide', 'pioglitazone', 'rosiglitazone', 'insulin']
    ordinal_orders = {'age': ['[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', '[50-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)'],
    'readmitted':['<30','>30','NO']}

    var_dict = {"int_columns": int_columns, "string_columns": string_columns, "ordinal_orders": ordinal_orders}

    diabetes = pd.read_csv("clean_diabetes.csv")
    # read the columns, then cast the types to simpler types
    diabetes[int_columns] = diabetes[int_columns].astype(int)
    diabetes[string_columns] = diabetes[string_columns].astype(str)

    for c in ordinal_orders:
        diabetes[c] = pd.Categorical(diabetes[c], categories=ordinal_orders[c], ordered=True)

    return diabetes, var_dict
