from bs4 import BeautifulSoup
import requests
import urllib.parse

base_url="https://search.naver.com/search.naver?where=post&sm=tab_jum&query="
plus_url=input()
my_url=base_url+urllib.parse.quote_plus(plus_url)

response=requests.get(my_url)
soup=BeautifulSoup(response.text, "html.parser")
text=soup.find_all("a", {"class":"sh_blog_title _sp_each_url _sp_each_title"})

for i in text:
    print(i['title'])







