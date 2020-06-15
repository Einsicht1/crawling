from bs4 import BeautifulSoup
import requests
import re
import csv
from selenium import webdriver
from time import sleep
import csv


sbuck = open("sbuck_menu.csv", "w+", encoding="utf-8")
wr = csv.writer(sbuck)
wr.writerow(('menu','img'))

driver = webdriver.Chrome("/Users/anna/crawling/chromedriver")
url = "https://www.starbucks.co.kr/menu/drink_list.do"

html = driver.get(url)      #스벅 크롬으로 키기. 이 다음에 스크롤 내리는게 들어가야 할듯.

max_page_height = int(driver.execute_script("return document.body.scrollHeight"))  #페이지 스크롤 맨아래까지 높이 구함.
window_page_height = int(driver.execute_script("return window.innerHeight"))       #윈도우 페이지 높이
upper = 0                                 #위 포지션
bottom = window_page_height               #아래 포지션
number = max_page_height // window_page_height

for i in range(number):
    driver.execute_script("window.scrollTo("+str(upper)+", " + str(bottom) + ");")
    upper += bottom
    bottom += bottom
    sleep(0.5)


req = driver.page_source #html따오는거.
#a =driver.find_element_by_css_selector('.goDrinkView img') #이걸로 li따와야되는데 수정해야됨.
soup = BeautifulSoup(req, "html.parser")
a = soup.find_all("a", {"class":"goDrinkView"})

for i in range(0,len(a)):
    print(a[i].find('img')['alt'])
    print(a[i].find('img')['src'])
    wr.writerow((a[i].find('img')['alt'],a[i].find('img')['src']))

driver.close()


#for i,value in enumerate(a):
 #   print(a[i].find_all('img'))
#print(img)
#for i in img:
#    print(i['src'])
#    print(i['alt'])


#<a href="javascript:void(0)" class="goDrinkView" prod="9200000002487"><img src="https://image.istarbucks.co.kr/upload/store/skuimg/2019/09/[9200000002487]_20190919181354811.jpg" alt="나이트로 바닐라 크림"></a>
#<img src="https://image.istarbucks.co.kr/upload/store/skuimg/2019/09/[9200000002487]_20190919181354811.jpg" alt="나이트로 바닐라 크림">
   #드라이버는 꼭 닫아주자. 크롬이 할때마다 켜져서 dock에 쌓임.


#SCROLL_PAUSE_TIME = 0.5
#SCROLL_LENGTH = 200
#page_height = int(driver.execute_script("return document.body.scrollHeight"))
#scrollPosition = 0
#while scrollPosition < page_height:
#    scrollPosition = scrollPosition + SCROLL_LENGTH
#    driver.execute_script("window.scrollTo(0, " + str(scrollPosition) + ");")
#    time.sleep(SCROLL_PAUSE_TIME)