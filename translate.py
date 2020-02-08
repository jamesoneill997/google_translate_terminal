from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
import time
import sys


chrome_options = Options()  
chrome_options.add_argument("--headless")  
browser = webdriver.Chrome("/home/James/Desktop/chromedriver", chrome_options = chrome_options)


#open requested page
browser.get("https://translate.google.com/")
time.sleep(1)

#change language to Spanish and send info
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[2]").click()
browser.find_element_by_xpath("//*[@id='source']").send_keys(input("Please enter what you would like to translate: "))

time.sleep(1)
translation = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]').text

print(translation)

