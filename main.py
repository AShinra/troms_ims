import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

def get_gsheet_client():
    # Load credentials from Streamlit secrets
    credentials_dict = {
        "type": st.secrets["gcp_service_account"]["type"],
        "project_id": st.secrets["gcp_service_account"]["project_id"],
        "private_key_id": st.secrets["gcp_service_account"]["private_key_id"],
        "private_key": st.secrets["gcp_service_account"]["private_key"],
        "client_email": st.secrets["gcp_service_account"]["client_email"],
        "client_id": st.secrets["gcp_service_account"]["client_id"],
        "auth_uri": st.secrets["gcp_service_account"]["auth_uri"],
        "token_uri": st.secrets["gcp_service_account"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["gcp_service_account"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["gcp_service_account"]["client_x509_cert_url"]
    }
    
    credentials = Credentials.from_service_account_info(credentials_dict, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    client = gspread.authorize(credentials)
    return client

def main():
    st.title("Google Sheets Access with Streamlit")
    
    try:
        client = get_gsheet_client()
        # sheet = client.open("Your Google Sheet Name").sheet1  # Update with your sheet name
        sheet_id = "1ZmilDNuV_h-w1OkKNwlbZCyD42KpaL5ilEK1hELRJpo"
        sheet = client.open_by_key(sheet_id)
        values_list = sheet.sheet1.row_values(1)
        st.write(values_list)
        sheet.sheet1.append_row([1,2,3,4])
    except Exception as e:
        st.error(f"Error accessing Google Sheet: {e}")

if __name__ == "__main__":
    main()