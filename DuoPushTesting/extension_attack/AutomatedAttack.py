import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://acadinfo.wustl.edu/WSHome/Default.aspx"

browser = webdriver.Firefox()
browser.get(link)

webstac_login_button = browser.find_element(By.ID, "ctl00_cphBody_btnLogin")
webstac_login_button.click()

time.sleep(5)

username_field = browser.find_element(By.ID, "ucWUSTLKeyLogin_txtUsername")
username_field.send_keys("e.j.palomino")

password_field = browser.find_element(By.ID, "ucWUSTLKeyLogin_txtPassword")
password_field.send_keys("Leo&klaus123")

connect_login_button = browser.find_element(By.ID, "ucWUSTLKeyLogin_btnLogin")
connect_login_button.click()

time.sleep(10)

soup = BeautifulSoup(browser.page_source, "html.parser")

verification_code_display = soup.find("div", class_="verification-code")
verification_code_number = verification_code_display.text.strip()

verification_device_display = soup.find("span", class_="phone-name")
verification_device_number = verification_device_display.text.strip()

print(verification_code_number)
print(verification_device_number)

browser.close()
