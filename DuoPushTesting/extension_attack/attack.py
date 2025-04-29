from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests

chrome_driver_path = "/Users/jackyang/Downloads/chromedriver/"  

driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://connect.wustl.edu/login/wulogin.aspx?idp_ver=3&execution=e2s1&ref=https://acadinfo.wustl.edu/"
driver.get(url)

def login(username, password):
    try:
        time.sleep(3)

        username_field = driver.find_element(By.NAME, "ucWUSTLKeyLogin_txtUsername") 
        password_field = driver.find_element(By.NAME, "ucWUSTLKeyLogin_txtPassword")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)
        print("Form submitted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def listen_for_credentials():
    server_url = "http://example.com/get-credentials"
    
    response = requests.get(server_url)
    if response.status_code == 200:
        data = response.json()
        username = data["ucWUSTLKeyLogin_txtUsername"]
        password = data["ucWUSTLKeyLogin_txtPassword"]
        print(f"Received credentials: {username}, {password}")
        login(username, password)
    else:
        print(f"Failed to receive credentials: {response.status_code}")

if __name__ == "__main__":
    listen_for_credentials()

    time.sleep(10) 
    driver.quit()
