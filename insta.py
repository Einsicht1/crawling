from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

base_url = "https://www.instagram.com/explore/tags/"
plus_url = input()
url = base_url + quote_plus(plus_url)


driver = webdriver.Chrome('/Users/anna/crawling/chromedriver' )

driver.get(url)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

insta = soup.select(".v1Nh3.kIKUG._bz0w")

n = 1
for i in insta:
    print('https://www.instagram.com'+ i.a['href'])
    imgUrl = i.img['src']
    with urlopen(imgUrl) as f:
      with open('./img2/' + plus_url + str(n)+ '.jpg', 'wb')as h:
           img = f.read()
           h.write(img)
    n += 1



driver.close()



