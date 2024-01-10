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

# Pieņemu visus sīkfailus.
find = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "onetrust-accept-btn-handler")))
find.click()

# Excel atveršana ar portfeļa datiem
file_path = "portfolio.xlsx"
df = pandas.read_excel(file_path)
portfolio = df.values.tolist()

current_price = []

for row in portfolio:

    # Mēģinu meklēt 2 klases, jo ir 2 veidu meklēšanas pogas atkarībā no pārlūkprogrammas loga izmēra.
    try:
        find = WebDriverWait(driver, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-aef7b723-0.fKbUaI")))

    except:
        find = WebDriverWait(driver, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-e20acb0c-1.fWcxPm")))

    find.click()

    # Meklēšanas loga ievadu kriptovalūtas nosaukumus.
    find = WebDriverWait(driver, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-8829bc3d-3.ikgYUd")))
    find.send_keys(row[1])
    time.sleep(1)
    find.send_keys(Keys.RETURN)

    # Atradu kriptovalūtas cenu un noņemu nevajadzīgus simbolus.
    find = WebDriverWait(driver, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-f70bb44c-0.jxpCgO.base-text")))
    temp = find.text.replace("$", "").replace(",", "")
    current_price.append(float(temp))
    print(current_price)

df['Current Price'] = current_price
df.to_excel(file_path, index=False)

driver.quit()
