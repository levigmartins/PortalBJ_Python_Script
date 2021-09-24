from requests.api import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#################################################### SETTINGS #########################################################

options = webdriver.ChromeOptions()
preferences = {"download.default_directory": "C:\\Users\\levig\\Downloads", "safebrowsing.enabled": "false"}
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome('C:/bin/chromedriver.exe',chrome_options=options)
email = "your_mail_here"
password = "your_password_here"

#################################################### DOWNLOAD #########################################################

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

# Acess "Relatórios" (Reports) page and waits for page to fully load
driver.get("https://portal.brasiljunior.org.br/relatorios")
sleep(2)

# Click on the 2021 report download button
driver.find_element_by_css_selector('#wrapper > div.content > div > div:nth-child(2) > div:nth-child(1) > div > div > div:nth-child(5) > a.btn.btn-primary.btn-sm').click()

#########################################################################################################################
