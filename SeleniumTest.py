from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.set_page_load_timeout(5)
driver.get("https://www.google.com")
driver.maximize_window()
#driver.find_element_by_name("q").send_keys("Automation Framework")
#driver.find_element_by_name("q").send_keys(Keys.ENTER)
searchBox = driver.find_element(By.XPATH, "//input[@name='q']")
searchBox.sendkeys("selenium")
searchBox.sendkeys(Keys.Enter)

#driver.close()
