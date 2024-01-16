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

# Sākotnējā ieguldījuma lieluma aprēķināšana un tās ierakstīšana Excel failā.
invested_amount = []

for row in portfolio:
    invested_amount.append(row[2] * row[3])

df['Invested amount, $'] = invested_amount
df.to_excel(file_path, index=False)

current_price = []
one_day = []
seven_days = []

for row in portfolio:

    # Mēģinu meklēt 2 klases, jo ir 2 veidu meklēšanas pogas atkarībā no pārlūkprogrammas loga izmēra.
    try:
        find = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "sc-aef7b723-0.fKbUaI")))

    except:
        find = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "sc-e20acb0c-1.fWcxPm")))

    find.click()

    # Meklēšanas loga ievadu kriptovalūtas nosaukumus.
    find = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-8829bc3d-3.ikgYUd")))
    find.send_keys(row[1])
    time.sleep(1)
    find.send_keys(Keys.RETURN)

    # Atradu kriptovalūtas cenu, noņemu nevajadzīgus simbolus un ierakstu cenu excel failā.
    find = WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "sc-f70bb44c-0.jxpCgO.base-text")))
    temp = find.text.replace("$", "").replace(",", "")
    current_price.append(float(temp))
    print(current_price)

    # Paņemu cenas izmaiņu par 1 dienu.
    time.sleep(1)
    find = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'sc-4984dd93-0.sc-58c82cf9-1.fwNMDM')))

    if "(1d)" in find.text:
        one_day.append(f'-{find.text}'.replace(" (1d)", ""))
    else:
        find = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'sc-4984dd93-0.sc-58c82cf9-1.heXOji')))
        one_day.append(f'+{find.text}'.replace(" (1d)", ""))

    # Paņemu cenas izmaiņu par 7 dienas.
    find = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, 'react-tabs-16')))
    find.click()

    find = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'sc-4984dd93-0.sc-58c82cf9-1.fwNMDM')))

    if "(7d)" in find.text:
        seven_days.append(f'-{find.text}'.replace(" (7d)", ""))
    else:
        find = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'sc-4984dd93-0.sc-58c82cf9-1.heXOji')))
        seven_days.append(f'+{find.text}'.replace(" (7d)", ""))
    print(seven_days)

df['Current Price, $'] = current_price
df.to_excel(file_path, index=False)

# Peļņas vai zaudējumu aprēķins no pirkuma cenas izmaiņām, procentos.
profit_loss = []
for row in portfolio:
    temp = ((row[5] - row[3]) / row[3]) * 100
    profit_loss.append(round(temp, 2))
print(profit_loss)

df['Profit / Loss, %'] = profit_loss
df.to_excel(file_path, index=False)

# Pašreizējais investīciju apjoms.
current_invest_amount = []
for row in portfolio:
    temp = (row[2] * row[5])
    current_invest_amount.append(round(temp, 2))
print(current_invest_amount)

df['Current Invested Amount, $'] = current_invest_amount
df.to_excel(file_path, index=False)

df['Price Change in 1 Day'] = one_day
df.to_excel(file_path, index=False)

df['Price Change in 7 Days'] = seven_days
df.to_excel(file_path, index=False)

driver.quit()