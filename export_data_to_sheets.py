from Google import Create_Service
import numpy as np
import json

# opens .json with authentication settings
with open("config.json") as jsonFile:
    Config = json.load(jsonFile)
    jsonFile.close()

sheet_id = Config["spreadsheet_id"]

# Receive my already filtered data and insert it in spreadsheet
def Export_Data_To_Sheets(filtered_file):
    
    # GOOGLE API SETTINGS
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    spreadsheet_id = sheet_id  # ID from sheet im updating

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES) # Creating Google Spreadsheet API service

    filtered_file.replace(np.nan, 'N/A', inplace=True) # Replace NaN with string 'N/A'

    # Update spreadsheet
    response_date = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        valueInputOption='RAW',
        range='bd!A1',
        body=dict(
            majorDimension='ROWS',
            values=filtered_file.T.reset_index().T.values.tolist())
    ).execute()