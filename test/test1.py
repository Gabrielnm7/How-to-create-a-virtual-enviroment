import time
import logging
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Configure the logging module to print only the level and the message
logging.basicConfig(level=logging.INFO)#, format='%(levelname)s: %(message)s')

# Arguments parser utility

driver_path = "C:\SeleniumDrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
login_payload = {"email":"ciro@smartgraphic.org", "password":"Romboost.123!"}

def check_rows(driver):
    # Adjust the selector to match your table rows
    rows = driver.find_element(By.ID, 'ctl00_MainContent_RadGrid1_ctl00').find_elements(By.TAG_NAME, 'tr')
    return len(rows) > 5000

def try_to_login():
    username_input = driver.find_element(By.ID, "MainContent_UserName")
    password_input = driver.find_element(By.ID, "MainContent_Password")

    username_input.clear()
    password_input.clear()

    username_input.send_keys(login_payload['email'])
    password_input.send_keys(login_payload['password'])

    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

max_attempts = 5
attempts = 0
# Login to the iBinderbook website  
driver.get("https://www.ibinderbook.com/app/Dashboard.aspx")


try:
    advanced_button = driver.find_element(By.ID, "details-button")
    advanced_button.click()
    proceed_link = driver.find_element(By.ID, "proceed-link")
    proceed_link.click()
except NoSuchElementException:
    pass

while attempts < max_attempts:
    try:
        try_to_login()
        attempts += 1
        # Wait for the popup to be visible with a timeout
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, 
                 "RadToolTipWrapper_ctl00_MainContent_RadToolTipSessionWarning")))
        yes_button = driver.find_element(By.ID, "MainContent_btnYes")
        yes_button.click()
        
    except NoSuchElementException:
        # If popup doesn't appear, break from the loop
        break
    except TimeoutException:
        # If wait times out, assume popup didn't appear and break from the loop
        break

if attempts >= max_attempts:
    msg = "Max login attempts reached. Login was not successful."
    logging.ERROR(msg)
    driver.quit()



# Wait for the table to load
wait = WebDriverWait(driver, 20)
date_input = wait.until(
    EC.presence_of_element_located(
        (By.ID, 
         "ctl00_MainContent_RadDatePickerFrom_dateInput")))
search_button = driver.find_element(By.ID, "ctl00_MainContent_btnFind")

# To select every record in time
date_input.clear()
date_input.send_keys("1/1/2022")

# To filter unneded status
status_combobox = driver.find_element(By.ID, "ctl00_MainContent_cboStatus_ClientState")
status_checked = [i for i in range(17)]

# Update the value attribute using JavaScript
script = "var element = arguments[0]; \
        var valueObject = JSON.parse(element.getAttribute('value')); \
        valueObject.checkedIndices = arguments[1]; \
        element.setAttribute('value', JSON.stringify(valueObject));"
driver.execute_script(script, status_combobox, status_checked)

search_button.click()
WebDriverWait(driver,240).until(check_rows)

table = driver.find_element(By.ID, 'ctl00_MainContent_RadGrid1_ctl00')
rows = table.find_elements(By.TAG_NAME, 'tr')
del table
headers = "ID;Date;Name;Email;Phone;Agent;Source;Status;Assign;User".split(';')
datetime_format = "%m/%d/%Y %I:%M:%S %p"

logging.info(f"{len(rows)} rows loaded in ram")

data = []
start = time.time()
logging.info(f"Starting to retrieve {len(rows[1:])} rows")
now = str(datetime.now())
logging.info("Starting at:", now)

print(rows[0].text)
driver.quit()