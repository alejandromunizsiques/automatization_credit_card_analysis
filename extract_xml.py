import selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import  dotenv_values

# envarioment variables being load from a .venv
config = dotenv_values(".env")

# start of the module based in funtions

def web_driver_initialzation(**kwargs): # funtion that start the webdriver and is directed to the initial page of the bank

    bank_url = kwargs.get("bank_url")

    driver = webdriver.Chrome()

    driver.get(bank_url)

    time.sleep(3)

    driver.find_element(By.XPATH, '//a[contains(@id,"ppp_header-link-banco_en_linea")]').click()

    return driver


def login_data(**kwargs): # this function is to log the data needed to enter to the bank account, its separated to the enter_page_account in case we need to repeat the log procces several times for pop ups or time outs

     driver = kwargs.get("driver")
     user_name = kwargs.get("user_name")
     password = kwargs.get("password")

     WebDriverWait(driver, 10).until(

          EC.presence_of_element_located((By.XPATH, '//input[contains(@class,"form-control ng-pristine ng-invalid ng-invalid-rut ng-invalid-required ng-valid-maxlength ng-touched") and contains(@placeholder, "Rut Usuario")]'))
     ).send_keys(user_name)
     WebDriverWait(driver, 10).until(

          EC.presence_of_element_located((By.XPATH, '//input[contains(@name,"userpassword") and contains(@placeholder, "Clave")]'))
     ).send_keys(password)
     time.sleep(1)

     driver.find_element(By.XPATH, '//button[contains(@class,"btn success btn-block") and contains(@id, "idIngresar")]').click()

     time.sleep(3)

     return driver


def enter_page_account(**kwargs):
     
     driver = kwargs.get("driver")
     user_name = kwargs.get("user_name")
     password = kwargs.get("password")


     try:
          login_data(driver = driver,
                     user_name = user_name,
                     password = password)
          

          try:
          
                re_login_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "Por favor intente ingresar nuevamente a nuestro portal.")]'))
                                                                  )
                
                if re_login_message:
                     
                     print("A re-log pop up showed up, initializing reload and relog proccess ")
                     driver.find_element(By.XPATH,'//button[contains(@class,"success btn pull-right") and contains(text, Ingresar)]').click()
                     login_data(driver = driver,
                                         user_name = user_name,
                                         password = password)
                     
          except NoSuchElementException:

               print("theres no pop up or reload and relog petition, initializing normally")
          
     except Exception as e:
          print("The login data procces failed")
          print(e)


     
     return driver


def download_excel(**kwargs):
     
     driver = kwargs.get("driver")

     WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, 
            '//span[contains(@class, "btn-text") and contains(text(), "SALDOS Y MOV.TARJETAS CRÉDITO")]'))
          ).click()
     
     time.sleep(2) 

     WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, 
            '//span[contains(@class, "btn-text") and contains(text(), "Descargar")]'))
          ).click()
     
     WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, 
            '//button[contains(@class, "bch-button-dropdown-menu-item") and contains(., "Descargar Excel")]'))
          ).click()


def account_operation(driver):
    try:
        # Intentar descargar el archivo Excel
        download_excel(driver=driver)

        try:
            
            pop_up_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, 
                    '//div[contains(@class, "cdk-overlay-pane modal-emergente") and contains(@class, "animate__slideInLeft")]'))
            )

            if pop_up_message:
                print("A re-log pop up showed up, initializing reload and re-login process.")
                
                WebDriverWait(driver, 10).until(
                     EC.presence_of_element_located((By.XPATH, 
                    '//button[contains(@class, "btn default btn pull-right") and contains(@onclick, "modal_emergente_close")]'))
                                              ).click()
        except NoSuchElementException:
            print("No pop-up detected, proceeding normally.")

    except Exception as e:
        print("The account operation has failed.")
        print(e)