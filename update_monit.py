from requests.api import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from export_data_to_sheets import Export_Data_To_Sheets

import os
import glob
import json
import pandas as pd

###################################################### SETTINGS #######################################################

options = webdriver.ChromeOptions()
preferences = {"download.default_directory": "C:\\Users\\levig\\Downloads", "safebrowsing.enabled": "false"}
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome('C:/bin/chromedriver.exe', options=options)

# opens .json with authentication settings
with open("config.json") as jsonFile:
    Config = json.load(jsonFile)
    jsonFile.close()

email = Config["email"]
password = Config["password"]

###################################################### DOWNLOAD #######################################################

# Access login page
driver.get("https://id.brasiljunior.org.br/sign-in")

# Search for the email input, wait for page to fully load and inputs the setted mail
mail_form = driver.find_element_by_css_selector('#__next > div > div > div > div > div.auth-box-action-block-ui > div > div.auth-box-action-body > form > div:nth-child(1) > div.form-float-label-wrapper > input')
sleep(1)
mail_form.send_keys(email)

# Search for the password input, wait for page to fully load and inputs the setted password
password_form = driver.find_element_by_css_selector('#__next > div > div > div > div > div.auth-box-action-block-ui > div > div.auth-box-action-body > form > div:nth-child(2) > div.form-float-label-wrapper > input')
sleep(1)
password_form.send_keys(password)

# Click on login button
driver.find_element_by_css_selector('#__next > div > div > div > div > div.auth-box-action-block-ui > div > div.auth-box-action-body > form > div.d-flex.justify-content-center > button').click()
sleep(2)

# Access "Relatórios" (Reports) page and waits for page to fully load
driver.get("https://portal.brasiljunior.org.br/relatorios")
sleep(2)

# Click on the 2021 report download button
driver.find_element_by_css_selector('#wrapper > div.content > div > div:nth-child(2) > div:nth-child(1) > div > div > div:nth-child(5) > a.btn.btn-primary.btn-sm').click()
sleep(30)

################################################ EXCEL FILE MANIPULATION ##############################################

list_of_files = glob.glob('C:\\Users\\levig\\Downloads\\*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime) # Return path to latest downloaded file (the report above)
sleep(5)

file_dict = pd.read_excel(latest_file, ['FEJEMG']) # Read tab 'FEJEMG' in downloaded report
file = pd.DataFrame.from_dict(file_dict['FEJEMG']) # Transform 'FEJEMG' tab dict into a DataFrame

filtered_file = file.loc[(file['NÚCLEO']=='Núcleo da Mata')] # Filters DF by column 'NÚCLEO'

############################################### GOOGLE SPREADSHEETS API ###############################################

try :
    Export_Data_To_Sheets(filtered_file) # Use already filtered data as parameter and update sheet by range
finally :
    driver.quit()