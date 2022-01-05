from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("https://www.google.com")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("Automation Framework")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
driver.close()
