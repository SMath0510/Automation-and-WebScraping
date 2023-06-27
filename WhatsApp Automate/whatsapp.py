import numpy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# import os
import time
from selenium.webdriver.common.keys import Keys


CHROME_DATA_PATH = "user-data-dir=C:\\Users\\shaun\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

# os.system("taskkill /im chrome.exe /f")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(CHROME_DATA_PATH)
driver = webdriver.Chrome(options= options, service=Service(ChromeDriverManager().install()), executable_path="C:\ProgramData\ChromeDriver\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
# driver.find_element(By.XPATH, '/html/body/ntp-app//div/cr-most-visited//div/a[1]/div[2]').click()
time.sleep(15)

def send_message(Name,message):
    search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
    search_box.send_keys(Name)
    time.sleep(2)
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]').click()
    time.sleep(2)
    
    message_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    message_box.send_keys(message)
    # message_box.send_keys(Keys.ENTER)
    print(f' The message{message} sent to {Name}')
    
Name = 'CP Community, IIT-M'
send_message(Name,"Test Message")
    