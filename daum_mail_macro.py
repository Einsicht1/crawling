from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Chrome("/Users/anna/crawling/chromedriver")
url = "https://www.daum.net/"
action = ActionChains(driver)
driver.get(url)

driver.find_element_by_css_selector(".link_login").click()
action.send_keys("kpl5672").send_keys(Keys.TAB).send_keys("Tenor!1692").perform()
action.reset_actions()
action = ActionChains(driver)
driver.find_element_by_css_selector("#loginBtn").click()

sleep(2)
driver.get("https://mail.daum.net/")
sleep(2)
driver.find_element_by_css_selector(".btn_comm.btn_write").click()
sleep(2)
(
action.send_keys("kpl5672@hanmail.net").send_keys(Keys.TAB)\
.send_keys(Keys.TAB).send_keys(Keys.TAB)\
.pause(2).send_keys("안녕하세요!")\
.send_keys(Keys.TAB).send_keys("반갑습니다.크롤링 테스트 중입니다.그럼 2000.")\
.perform()
)
driver.find_element_by_css_selector(".btn_toolbar.btn_write").click()


# action.reset_actions()
# driver.find_element_by_css_selector(".RveJvd.snByac").click()