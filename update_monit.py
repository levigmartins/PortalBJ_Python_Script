from requests.api import options
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

preferences = {"download.default_directory": "C:/Users/levig/Downloads"}

options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome('C:/bin/chromedriver.exe',chrome_options=options)

driver.get("https://portal.brasiljunior.org.br/relatorios")
driver.find_element(By.XPATH, "//*[@id='wrapper']/div[2]/div/div[2]/div[1]/div/div/div[4]/a[1]").click()
