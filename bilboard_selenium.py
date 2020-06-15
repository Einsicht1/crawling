from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv
file_name = "bbd_final.csv"
csv_open = open(file_name, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('rank','song','singer','img'))




chrome = webdriver.Chrome("/Users/anna/crawling/chromedriver")
chrome.get("https://www.billboard.com/charts/hot-100")

body = chrome.find_element_by_css_selector("body")
keys = body.send_keys(Keys.PAGE_DOWN)
for i in range(100):
    body.send_keys(Keys.PAGE_DOWN)

ol = chrome.find_elements_by_class_name("chart-list__element")

for i in ol:
    rank = i.find_element_by_class_name("chart-element__rank__number").text
    song = i.find_element_by_class_name("chart-element__information__song").text
    singer = i.find_element_by_class_name("chart-element__information__artist").text
    img = i.find_element_by_class_name("chart-element__image")
    a = img.get_attribute('style')[23:]
    b = a[:-3]
    csv_writer.writerow((rank,song,singer,b))



# rank = chrome.find_elements_by_class_name("chart-element__rank__number")
# song = chrome.find_elements_by_class_name("chart-element__information__song")
# singer = chrome.find_elements_by_class_name("chart-element__information__artist")
# img = chrome.find_elements_by_class_name("chart-element__image")
# for i in rank:
#      print(i.text)
#      csv_writer.writerow()
#
# for i in singer:
#      print(i.text)
#
# for i in singer:
#      print(i.text)
#
# for i in img:
#     a = i.get_attribute('style')[23:]
#     b = a[:-3]
#     print(b)


chrome.quit()

