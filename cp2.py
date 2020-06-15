from bs4 import BeautifulSoup
import requests
import re
import csv

excel = open("fashion.csv","w+",encoding="utf-8")
wr=csv.writer(excel)
wr.writerow(('title','img-url'))



url = "http://www.vogue.co.kr/category/fashion/"
url_get=requests.get(url)
soup = BeautifulSoup(url_get.text, "html.parser")
article = soup.find_all('article', {'id':re.compile('post-*')})
for i in article:
    h2=i.find('h2')
    text=h2.get_text()
    print(text)
    img = i.find('img')
    print(img['src'])
    wr.writerow((text,img['src']))

excel.close()







