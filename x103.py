# actually is x106 just that the streamlit thing doesn't allow to change the filename
import streamlit as st

pg = st.navigation([st.Page("x105SingleVariables.py",title='Numerical variables'),
                    st.Page("x105Correlations.py", title='Correlations')])
pg.run()