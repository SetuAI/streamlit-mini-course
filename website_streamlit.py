import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Simple data dashboard")

uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data preview")
    
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value",unique_values)
    
    # display
    filtered_df = df[df[selected_column] == selected_value]
    
    st.write(filtered_df)
    
    # plot this
    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column",columns)
    y_column = st.selectbox("Select Y-axis column",columns)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
        
    else:
        st.write("Waiting on file upload ..")


    
    
    
