import streamlit as st
import pandas as pd
from datetime import datetime

# Function to process the uploaded Excel file
def process_excel_file(file):
    try:
        # Read the Excel file
        df = pd.read_excel(file, sheet_name='Additions and Modification')

        # Extract 'Lessor Name' and 'EndDate' columns
        if 'Lessor Name' in df.columns and 'EndDate' in df.columns:
            df_result = df[['Lessor Name', 'EndDate']]

            # Convert 'EndDate' column to datetime
            df_result['EndDate'] = pd.to_datetime(df_result['EndDate'], errors='coerce')

            # Create 'lease expired' column
            df_result['lease expired'] = df_result['EndDate'].apply(
                lambda x: 'Yes' if datetime.now() > x else 'No' if pd.notnull(x) else ''
            )

            return df_result
        else:
            st.error("Required columns not found in the sheet.")
            return None

    except Exception as e:
        st.error(f"Error processing the Excel file: {e}")
        return None

# Streamlit app
def main():
    st.title("Lease Information App")
    
    # Upload Excel file
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])
    
    if uploaded_file is not None:
        # Process the Excel file
        result_df = process_excel_file(uploaded_file)

        # Display the result
        if result_df is not None:
            st.subheader("Resulting DataFrame:")
            st.write(result_df)

# Run the app
if __name__ == "__main__":
    main()
