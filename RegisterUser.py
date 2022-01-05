from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("https://askomdch.com/")
driver.maximize_window()
# finding the element and filling the form
# find the Account Link for Account Registration
# Click on Account link
driver.find_element(By.XPATH, "//a[text()='Account']").click()
# Move to Login/Registration Page
# Find the username text box and wait till element to be clickable
element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "reg_username")))
element.send_keys("Shah2020")
# Find the email text box
#element = WebDriverWait(driver, 20).until(EC.element_located_to_be_selected((By.ID, "reg_email")))
element=driver.find_element(By.ID, "reg_email")
element.send_keys("Test@gmail.com")
# Find the password text box
#element = WebDriverWait(driver, 20).until(EC.element_located_to_be_selected((By.ID, "reg_password")))
element=driver.find_element(By.ID, "reg_password")
element.send_keys("Test@2022")
# //button[@type='submit'  and  @value='Register']
#element = WebDriverWait(driver, 20).until(EC.element_located_to_be_selected((By.XPATH, "//button[@type='submit'  and  @value='Register']")))
element=driver.find_element(By.XPATH, "//button[@type='submit'  and  @value='Register']")
element.click()
driver.close()
