import  extract_xml
from dotenv import  dotenv_values
config = dotenv_values(".env")


try:

   driver = extract_xml.web_driver_initialzation(bank_url =config["BANK_URL"] )

except Exception as e:

    print("the inizalization of the driver failed")
    print(e)

try:

    extract_xml.enter_page_account( driver = driver,
                            user_name = config["USER_NAME"],
                            password = config["PASSWORD"] )
except Exception as e:

    print("the account enter_page step has failed, error log:")
    print(e)

try:
    extract_xml.account_operation(driver = driver)

except Exception as e:
    print("the account operation proccess has filed, error log")
    print(e)



