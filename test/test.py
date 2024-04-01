from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

login = {"username": "41586382", "password": "savino20"}

driver_path = "C:\SeleniumDrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://campus.exactas.uba.ar/login/index.php")

driver.find_element_by_id("username").send_keys(login["username"])
driver.find_element_by_id("password").send_keys(login["password"])

login_button = driver.find_element_by_id("loginbtn")
login_button.click()
time.sleep(1)
driver.get("https://campus.exactas.uba.ar/my/")
time.sleep(0.5)
driver.get("https://campus.exactas.uba.ar/pluginfile.php/549664/mod_resource/content/2/practica2-ldd-1c2024.pdf")
time.sleep(2)


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, 
         "ENCONTRAR EL PUTO BOTON DE DESCARGAAAAAAR")))

driver.quit()