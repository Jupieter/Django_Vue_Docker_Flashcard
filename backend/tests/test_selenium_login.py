from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Selenium webdriver inicializálása
driver = webdriver.Chrome()

# Weboldal betöltése
driver.get('http://localhost:5173/')

# Felhasználónév és jelszó bevitel
username_input = driver.find_element(By.ID, 'form-username')
password_input = driver.find_element(By.ID, 'form-password')
username_input.send_keys('Test2')
password_input.send_keys('jelszo2')

# Bejelentkezés gombra kattintás
login_button = driver.find_element(By.ID, 'btn_login_submit')
login_button.click()
sleep(5)
# Várakozás a bejelentkezés befejeződésére
driver.implicitly_wait(5)

# Teszt eredményének ellenőrzése
# assert 'Belépve' in driver.page_source

# WebDriver bezárása
# driver.quit()

