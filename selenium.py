from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os 

html_path='file://'+ os.path.abspath('websayfasıtest.html')
driver=webdriver.Chrome() #tarayıcıyı kontrol eden nesne
driver.get(html_path)

time.sleep(5)

username_input=driver.find_element(By.ID, "username")
username_input.send_keys('sylaork')
#username_input.send_keys(Keys.RETURN)

time.sleep(5)

password_input=driver.find_element(By.ID, "password")
password_input.send_keys("silasila")
#password_input.send_keys(Keys.RETURN)

time.sleep(5)

button=driver.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(10)


driver.quit()
