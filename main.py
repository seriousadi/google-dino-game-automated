from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image

driver = webdriver.Chrome()
game_on = True
driver.get('https://elgoog.im/t-rex/')
driver.implicitly_wait(5)
#driver.execute_script("document.body.style.zoom='50%'")
#sleep(2)
driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.SPACE)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]').screenshot(filename='screenshot.png')
image = Image.open('screenshot.png')
cropped = image.crop((80, 100, 120, 125))
cropped_colors = cropped.convert('RGB').getcolors()
if len(cropped_colors) > 1:
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.SPACE)