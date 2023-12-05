import streamlit as st
from streamlit.components.v1 import html
from dashboard import dash as dashboard_main  # Assuming your dashboard file has a main function



def main():
   

    # Use the provided HTML component for authentication


    # Streamlit input components for email and password
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Button to trigger authentication
    if st.button("Login"):
        if authenticate_user(email, password):
            st.success("Login successful!")
            # Call the main function from the dashboard file
            dashboard_main()
        else:
            st.error("Invalid credentials. Please try again.")

def authenticate_user(email, password):
    """
    Perform user authentication. Replace with your secure authentication logic.
    """
    # Hardcoded credentials for demonstration purposes
    valid_credentials = {
        "ficyoncube47@gmail.com": "12345",
        "ketso014@gmail.com": "12345",
    }

    if email in valid_credentials and valid_credentials[email] == password:
        return True
    else:
        return False

if __name__ == "__main__":
   main()
