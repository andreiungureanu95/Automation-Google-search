from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C://chromedriver.exe')
driver.get('https://www.reserved.com/ro/ro/?gclid=CjwKCAiA7dKMBhBCEiwAO_crFF3WwCkzViZO-8q3IuHudRKHK_gLtf4T7-zW2c_MGFPIMi6hYeVa_RoCoSYQAvD_BwE')

driver.maximize_window()

sleep(1)



account = driver.find_element(By.XPATH, '//*[@id="headerWrapper"]/div/div[3]/div[2]').click()

sleep(1)
driver.get("https://www.reserved.com/ro/ro/customer/account/login/#register")
sleep(1)

createAccount = driver.find_element(By.XPATH,'//*[@id="email_id"]')
emailInput = driver.find_element(By.XPATH,'//*[@id="email_id"]').send_keys("mihai@reserved.com")
FirstNameInput = driver.find_element(By.XPATH,'//*[@id="firstname_id"]').send_keys("Mihai")
LastNameInput = driver.find_element(By.XPATH,'//*[@id="lastname_id"]').send_keys("Popescu")
passwordInput = driver.find_element(By.XPATH,'//*[@id="password_id"]').send_keys("Abc.1234")
checkBox = driver.find_element(By.CSS_SELECTOR,'#is_subscribed_id').click()
sleep(2)
createAccountLast = driver.find_element(By.CSS_SELECTOR,'#loginRegisterRoot > div > div.sc-dVNiOx.eRoZWc > div > form > button').click()
sleep(1)

driver.close

print("Congrats!")


