import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request

driver = webdriver.Chrome()

driver.get("http://localhost:9999/scrolltoload.html")
time.sleep(10)
driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)

for i in range(1, 21):
    driver.find_element_by_tag_name("html").get_attribute("src")
    url = driver.find_element_by_xpath(f"//div/div[{i}]/img").get_attribute("src")

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    name = driver.find_element_by_xpath(f'//div/div[{i}]/img/following-sibling::p').text
    name = name[8:]

    local = f'cats/{i}-{name}.jpg'
    urllib.request.urlretrieve(url, local)

driver.close()
