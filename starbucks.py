from bs4 import BeautifulSoup
import requests
import re
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

url = "https://www.starbucks.co.kr/menu/drink_list.do"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup)



