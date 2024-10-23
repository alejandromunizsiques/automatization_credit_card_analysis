import  extract_xml
from dotenv import  dotenv_values
config = dotenv_values(".env")


try:

   driver = extract_xml.web_driver_initialzation(bank_url =config["BANK_URL"] )

except Exception as e:

    print("the inizalization of the driver failed")
    print(e)

try:

    extract_xml.login_user( driver = driver,
                            user_name = config["USER_NAME"],
                            password = config["PASSWORD"] )
except Exception as e:

    print("the login procces had failed")
    print(e)

try:
    extract_xml.download_excel(driver = driver)

except Exception as e:
    print("the extraction proccess had filed")
    print(e)



