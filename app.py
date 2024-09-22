# app.py

# Import necessary libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit app title
st.title('Correlation Heatmap App')

# Upload parquet file
uploaded_file = st.file_uploader("Upload a Parquet file", type=["parquet"])

if uploaded_file is not None:
    # Load the parquet file into a DataFrame
    df = pd.read_parquet(uploaded_file)

    # Display the DataFrame as a preview
    st.write("### Data Preview")
    st.write(df.head())

    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    if numeric_df.empty:
        st.write("No numeric columns available for correlation.")
    else:
        # Generate and display the correlation heatmap
        st.write("### Correlation Heatmap")

        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
        plt.title('Correlation Heatmap of DataFrame Columns (Subset)')
        
        st.pyplot(fig)
