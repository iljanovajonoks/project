import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://coinmarketcap.com/"
driver.get(url)

# Mēģinu meklēt 2 klases, jo ir 2 veidu meklēšanas pogas atkarībā no pārlūkprogrammas loga izmēra.
try:
    find = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-aef7b723-0.fKbUaI")))

except:
    find = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-e20acb0c-1.fWcxPm")))

find.click()

input()