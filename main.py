from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pandas

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://coinmarketcap.com/"
driver.get(url)

file = pandas.read_excel("portfolio.xlsx")
portfolio = file.values.tolist()

current_pice = []
for row in portfolio:

    # Mēģinu meklēt 2 klases, jo ir 2 veidu meklēšanas pogas atkarībā no pārlūkprogrammas loga izmēra.
    try:
        find = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-aef7b723-0.fKbUaI")))

    except:
        find = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-e20acb0c-1.fWcxPm")))

    find.click()

    find = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-8829bc3d-3.ikgYUd")))
    find.send_keys(row[1])
    time.sleep(1)
    find.send_keys(Keys.RETURN)
    find = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-f70bb44c-0.jxpCgO.base-text")))
    temp = (find.text).replace("$", "").replace(",", "")
    current_pice.append(float(temp))
    print(current_pice)
input()