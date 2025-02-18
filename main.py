import streamlit as st
import gspread
from google.oauth2.service_account import Credentials




if __name__ == '__main__':
    print('test')

    scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
    ]

    credentials = st.secrets

    # creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    creds = Credentials.from_service_account_file(credentials, scopes=scopes)
    client = gspread.authorize(creds)

    sheet_id = "1ZmilDNuV_h-w1OkKNwlbZCyD42KpaL5ilEK1hELRJpo"
    sheet = client.open_by_key(sheet_id)

    values_list = sheet.sheet1.row_values(1)
    st.write(values_list)