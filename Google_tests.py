from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# initialize chrome driver
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# Go to url
driver.get("https://google.ro")

# maximize
driver.maximize_window()

# refresh page
driver.refresh()
sleep(1)

# delete cookies
driver.delete_all_cookies()

# # find an element by xpath - and click
# see the black text in html page and see in the in interface
driver.find_element_by_xpath("//div[text()='Sunt de acord']").click()

# find element by attribute name name and send values from keyboard
# input is the web element (ROZ)
# name is the attribute of input (ORANGE)
# q e value of the attribute name (ALBASTRU)
search_input = driver.find_element_by_name("q")

# values from keyboard in input
search_input.send_keys("automation")
sleep(2)

# delete values from input with clear()
search_input.clear()
sleep(2)

# send values in search box
search_input.send_keys("Automation")
sleep(2)

# press  (ENTER)
search_input.send_keys(Keys.ENTER)

# get and verify url
url = driver.current_url
print(url)
assert url.__contains__("search?q=automation")

# get and verify page title
title = driver.title
print(title)
assert title == "automation - Căutare Google"

# navigate back
driver.back()

# verify text on Submit button
submit_btn = driver.find_element_by_name("btnK")
assert submit_btn.get_attribute("aria-label") == "Căutare Google"
assert submit_btn.get_attribute("value") == "Căutare Google"

# verify text on Lucky button
lucky_btn = driver.find_element_by_name("btnI")
assert lucky_btn.get_attribute("aria-label") == "Mă simt norocos"
assert lucky_btn.get_attribute("value") == "Mă simt norocos"

# close chrome
sleep(2)
driver.close()