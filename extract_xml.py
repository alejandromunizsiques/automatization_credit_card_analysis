import selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import  dotenv_values

# envarioment variables being load from a .venv
config = dotenv_values(".env")

# start of the module based in funtions

def web_driver_initialzation(**kwargs): # funtion that start the webdriver and is directed to the initial page of the bank

    bank_url = kwargs.get("bank_url")

    driver = webdriver.Chrome()

    driver.get(bank_url)

    time.sleep(3)

    return driver


def login_user(**kwargs):
     
     driver = kwargs.get("driver")
     user_name = kwargs.get("user_name")
     password = kwargs.get("password")

     if driver.find_element(By.XPATH, '//p[contains(text,"Por favor intente ingresar nuevamente a nuestro portal.")]'):
          driver.find_element(By.XPATH,'//button[contains(@class,"success btn pull-right")]')








     driver.find_element(By.XPATH, '//a[contains(@id,"ppp_header-link-banco_en_linea")]').click()
     time.sleep(1)
     driver.find_element(By.XPATH, '//input[contains(@class,"form-control ng-pristine ng-invalid ng-invalid-rut ng-invalid-required ng-valid-maxlength ng-touched") and contains(@placeholder, "Rut Usuario")]').send_keys(user_name)
     time.sleep(1)
     driver.find_element(By.XPATH, '//input[contains(@name,"userpassword") and contains(@placeholder, "Clave")]').send_keys(password)
     time.sleep(1)
     driver.find_element(By.XPATH, '//button[contains(@class,"btn success btn-block") and contains(@id, "idIngresar")]').click()
     time.sleep(3)

def download_excel(**kwargs):
     
     driver = kwargs.get("driver")
     driver.find_element(By.XPATH,'//span[contains(@class, "btn-text") and contains(text(), "SALDOS Y MOV.TARJETAS CRÉDITO")]').click()
     time.sleep(2) 
     driver.find_element(By.XPATH,'//span[contains(@class, "btn-text") and contains(text(), "Descargar")]').click()

