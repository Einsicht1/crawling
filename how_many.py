from selenium import webdriver
from selenium.webdriver.common.keys import Keys
name = input('주소입력')
driver = webdriver.Chrome("/Users/anna/crawling/chromedriver")
driver.get(f"https://velog.io/@{name}")

body = driver.find_element_by_css_selector("body")
keys = body.send_keys(Keys.PAGE_DOWN)
for i in range(5000):
    keys = body.send_keys(Keys.PAGE_DOWN)

a= driver.page_source
b = len(driver.find_elements_by_class_name("subinfo"))
print(f"블로그 쓰신 갯수는 {b}개 입니다")


driver.quit()

