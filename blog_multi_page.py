from bs4 import BeautifulSoup
import requests
import urllib.parse

plusurl = urllib.parse.quote_plus(input('검색어 입력하세요'))
i = input("몇페이지까지 출력 하실래요?")

num = 1
n = 1
last_page = int(i) * 10 - 9
while num <= last_page:
    
    url = f"https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusurl}&srchby=all&st=sim&where=post&start={num}"
    html = requests.get(url)
    url_text = html.text
    soup = BeautifulSoup(url_text, "html.parser")
    text = soup.find_all("a", {"class":"sh_blog_title _sp_each_url _sp_each_title"})
    print(f"{n}페이지 내용입니다---------")
    for i in text:
        print(i.text)
        print(i['href'])
        print()
    n += 1
    num += 11
    





