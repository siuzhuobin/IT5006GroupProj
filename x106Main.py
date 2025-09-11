import streamlit as st

pg = st.navigation([st.Page("x106Overview.py",title='Basic Information'),
                    st.Page("x106TargetAnalysis.py", title='Target Distribution Analysis'),
                    st.Page("x106NumericalFeatures.py", title='Numerical Feature Analysis'),
                    st.Page("x106CategoricalFeatures.py", title='Categorical Feature Analysis'),
                    st.Page("x106FeatureCorrelation.py", title='Feature Correlation Analysis')
                    ])
pg.run()