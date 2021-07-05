import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

videoref = ['iframe', "//*[@id='html5video']", "//button[@onclick='playPause()']"]

driver = webdriver.Chrome()
driver.get("http://localhost:9999/videos.html")


driver.find_element_by_xpath('//button[@onclick="playPause()"]').send_keys(Keys.SPACE)
time.sleep(2)
driver.find_element_by_xpath('//button[@onclick="playPause()"]').send_keys(Keys.SPACE)

driver.find_element_by_xpath("//*[@id='html5video']").send_keys(Keys.SPACE)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='html5video']").send_keys(Keys.SPACE)

frame = driver.find_element_by_id('youtubeframe')
driver.switch_to.frame(frame)
driver.find_element_by_class_name("ytp-large-play-button.ytp-button").send_keys(Keys.SPACE)
time.sleep(5)
driver.find_element_by_xpath('//button[@class="ytp-play-button ytp-button"]').send_keys(Keys.SPACE)

driver.close()