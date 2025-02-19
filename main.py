import streamlit as st
from streamlit_option_menu import option_menu
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

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
    st.title("JFM Inventory Management")

    with st.container(border=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            _date = st.date_input('Delivery Date').isoformat()
            _item = st.text_input('Item')
        with col2:
            _brand = st.text_input('Brand')
            _desc = st.text_input('Description')
        with col3:
            _qty = st.number_input('Quantity', step=1)
            _unit = st.selectbox('Unit', options=['pouch', 'sack', 'box', 'pcs', 'can'])
        st.button('Add' , key='add_item')
    
    try:
        client = get_gsheet_client()
        # sheet = client.open("Your Google Sheet Name").sheet1  # Update with your sheet name
        sheet_id = "1ZmilDNuV_h-w1OkKNwlbZCyD42KpaL5ilEK1hELRJpo"
        sheet = client.open_by_key(sheet_id)
        # values_list = sheet.sheet1.row_values(1)
        # st.write(values_list)

    except Exception as e:
        st.error(f"Error accessing Google Sheet: {e}")

    if st.session_state['add_item']:
        sheet.sheet1.append_row([_date, _item, _brand, _desc, _qty, _unit])
        # .append_row(_date, _item, _desc, _qty)

    data = sheet.sheet1.get_all_values()

    df = pd.DataFrame(data)
    df.columns = df.iloc[0]
    df = df[1:]
    st.dataframe(df, use_container_width=True)


if __name__ == "__main__":

    with st.sidebar:
        selected = option_menu("Inventory Menu", ["Delivery", 'Set Out', 'Inventory'], 
        icons=['truck', 'basket', 'bank'], menu_icon="cast", default_index=1)
        
    main()