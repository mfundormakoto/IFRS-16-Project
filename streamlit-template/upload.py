import streamlit as st
import PyPDF2
import os
import base64

# Define ButtonMixin class
class ButtonMixin:
    def download_button(self, label, key, file_path):
        return st.button(
            label=label,
            key=key,
            on_click=lambda: st.markdown(
                f'<a href="data:application/octet-stream;base64,{base64.b64encode(open(file_path, "rb").read()).decode()}" download="{os.path.basename(file_path)}">Download File</a>',
                unsafe_allow_html=True,
            )
        )

# Function to save the uploaded PDF file to a folder
def save_uploaded_file(uploaded_file):
    folder_path = os.path.join(os.getcwd(), "uploads")
    os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
    with open(os.path.join(folder_path, uploaded_file.name), "wb") as file:
        file.write(uploaded_file.getbuffer())

# Function to list available PDF files in the uploads folder
def list_uploaded_files():
    folder_path = os.path.join(os.getcwd(), "uploads")
    return os.listdir(folder_path)

# Main Streamlit app
def main():
    st.title("PDF File Viewer and Storage")

    # Upload PDF file
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Save uploaded file
        save_uploaded_file(uploaded_file)
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    # Display uploaded file history
    st.subheader("Uploaded Files:")
    uploaded_files = list_uploaded_files()

    if not uploaded_files:
        st.info("No files uploaded yet.")
    else:
        selected_file = st.selectbox("Select a file for download:", uploaded_files)
        file_path = os.path.join(os.getcwd(), "uploads", selected_file)

        # Create an instance of ButtonMixin
        button_mixin = ButtonMixin()

        # Use download_button method to create the download button
        button_mixin.download_button(
            label="Download Selected File",
            key="download_button",
            file_path=file_path,
        )

if __name__ == "__main__":
    main()
