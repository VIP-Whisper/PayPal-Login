from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
email='email'
psw='password'
driver = webdriver.Chrome()
driver.get("https://www.paypal.com/signin")
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
email_element = driver.find_element(By.ID, "email")
email_element.send_keys(email)
btn_next = driver.find_element(By.ID, "btnNext")
btn_next.click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
password_element = driver.find_element(By.ID, "password")
password_element.send_keys(psw)
btn_login = driver.find_element(By.ID, "btnLogin")
btn_login.click()
source = driver.page_source
if "Security Challenge" in source or "Some of your info isn't correct." in source in source:
    print("Error")
elif "For security reasons, you’ll need to" in source:
 print('OTP')