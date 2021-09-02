from selenium import webdriver
from time import sleep

# initialize chromedriver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# Go to url
driver.get("https://www.jules.app")

sleep(1)

# maximize
driver.maximize_window()

# identify an element by value of an attribute and send the values from keyboard
driver.find_element_by_xpath("//input[@placeholder='Enter your email']").send_keys("andrei@abc.com")
sleep(1)

driver.find_element_by_xpath("//input[@type='password']").send_keys("pass123")

# identify an element by text and click on
driver.find_element_by_xpath("//span[text()='Log in']").click()
sleep(2)

# check the error message
error = driver.find_element_by_xpath("//span[text()='Invalid email/password combination']")
assert error.is_displayed() is True

# close chrome
driver.close()