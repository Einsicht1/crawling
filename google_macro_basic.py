from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/anna/crawling/chromedriver")

url = "https://www.google.co.kr/"
driver.get(url)

driver.find_element_by_css_selector(".gLFyf.gsfi").send_keys("파이썬")
driver.find_element_by_css_selector(".gLFyf.gsfi").send_keys(Keys.ENTER)

driver.find_element_by_css_selector(".LC20lb.DKV0Md").click()
driver.back()
driver.forward()
driver.execute_script("window.history.go(-1)")
driver.quit()


