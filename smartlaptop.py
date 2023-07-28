from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service(r"C:\Users\lenovo\Desktop\chromedriver.exe")

# set the different options for the browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# ignore the certificate and SSL errors
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
# maximize the browser window
chrome_options.add_argument("start-maximized")
# define with the driver and open the browser
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get('https://www.smartprix.com/laptops')
time.sleep(1)

driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)

driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')

while True :

    driver.find_element(by=By.XPATH, value = '//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')
    print(old_height)
    print(new_height)

    if new_height == old_height :
        break

    old_height = new_height

html =driver.page_source

with open('smartprixlaptop.html', 'w', encoding ='utf-8') as f:
    f.write(html)
