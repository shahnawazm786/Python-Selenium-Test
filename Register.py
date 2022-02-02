from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



#driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
ser = Service("Drivers\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
#driver.set_page_load_timeout(5)
driver.get("https://askomdch.com/account/")
driver.maximize_window()
userName=driver.find_element(By.ID, 'reg_username')
userName.sendkeys("Mohammad")
userEmail=driver.find_element(By.NAME, "email")
userEmail.sendkeys("mohammad@gmail.com")
userPassword=driver.find_element(By.ID, "reg_password")
userPassword.sendkeys("Shah@1234")
btnRegister=driver.find_element(By.NAME, "register")
btnRegister.click()
driver.close()