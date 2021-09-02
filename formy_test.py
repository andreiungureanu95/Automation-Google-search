from cProfile import label

import menu as menu
from selenium import webdriver

from time import sleep

# initializam un obiect de tip chromedriver
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")

# navigate to url

driver.get("http://formy-project.herokuapp.com/form")

#minimize

driver.minimize_window()


# maximize

driver.maximize_window()

# Send from keyword to input

driver.find_element_by_xpath("//input[@id='first-name']").send_keys("Mihai")



driver.find_element_by_xpath("//input[@placeholder='Enter last name']").send_keys("Popescu")



driver.find_element_by_id("job-title").send_keys("Software Developer")

#check bullet buttons

driver.find_elements_by_xpath("//input[@type = 'radio']")[0].click()
driver.find_elements_by_xpath("//input[@type = 'radio']")[1].click()
driver.find_elements_by_xpath("//input[@type = 'radio']")[2].click()

#check check cases

driver.find_elements_by_xpath("//input[@type='checkbox']")[0].click()
driver.find_elements_by_xpath("//input[@type='checkbox']")[1].click()
driver.find_elements_by_xpath("//input[@type='checkbox']")[2].click()

#select from list

driver.find_elements_by_xpath("//select[@class='form-control']")[0].click()

select.select_by_visible_text('0-1')


#click on submit

driver.find_element_by_xpath("//a[text()='Submit']").click()

#check done
sleep(3)

url=driver.current_url
print("http://formy-project.herokuapp.com/thanks")

# check if the url contain /thanks

assert url.__contains__("/thanks")

text = driver.find_element_by_xpath("//h1").text
assert text == "Thanks for submitting your form"
#driver.close()
