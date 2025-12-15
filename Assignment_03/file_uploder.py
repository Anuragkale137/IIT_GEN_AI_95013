#Upload a CSV file. Input a SQL query from user and execute it on the CSV data (as dataframe ). Display result on the

import pandas as pd
import streamlit as st
import sqlite3

st.title("CSV SQL Query Executor")
uploaded_file = st.file_uploader("Upload your csv file",type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dataframe preview:")
    st.dataframe(df.head())
    con=sqlite3.connect(':memory:')
    df.to_sql("df", con,index=False, if_exists="replace")

    query = st.text_area("Enter your SQl query here (use 'df' as the dataframe name):",height = 150)
    if st.button("Execute Query"):
        try:
            result = pd.read_sql_query(query, con, params={'df':df})
            st.write("Query Result:")
            st.dataframe(result)
        except Exception as e:
            st.error(f"An error occured:{e}")