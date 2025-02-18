import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import json
import toml
import os


def convert_toml_to_json(toml_file, json_file):
    """Converts a TOML file to JSON format."""
    try:
        with open(toml_file, 'r') as f:
            toml_data = toml.load(f)
        
        with open(json_file, 'w') as f:
            json.dump(toml_data, f, indent=4)
        
        print(f"Successfully converted {toml_file} to {json_file}")
    except Exception as e:
        print(f"Error: {e}")
    
    return json_file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        



if __name__ == '__main__':
    
    scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
    ]

    _path = os.getcwd()
    _file = f"{_path}/credentials.json"

    credentials = convert_toml_to_json(st.secrets, _file)
    # st.write(credentials.json)

    creds = Credentials.from_service_account_file(_file, scopes=scopes)
    client = gspread.authorize(creds)

    sheet_id = "1ZmilDNuV_h-w1OkKNwlbZCyD42KpaL5ilEK1hELRJpo"
    sheet = client.open_by_key(sheet_id)

    values_list = sheet.sheet1.row_values(1)
    st.write(values_list)