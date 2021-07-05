import datetime

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/forms.html")

driver.find_element_by_id("example-input-date").send_keys(datetime.datetime.now().strftime(f"00%YYYY/%m/%d"))

driver.find_element_by_id("example-input-date-time").send_keys(
    datetime.datetime.now().strftime(f"%Y.%m.%d %H:%M:%S:%f"))

driver.find_element_by_id("example-input-date-time-local").send_keys(
    datetime.datetime.now().strftime(f"00%YYYY/%m/%d%I:%M"))

driver.find_element_by_id("example-input-month").send_keys(datetime.datetime.now().strftime(f"%Y%B"))

driver.find_element_by_id("example-input-week").send_keys(datetime.datetime.now().strftime(f"%U%Y "))

driver.find_element_by_id("example-input-time").send_keys(datetime.datetime.now().strftime(f"%I:%M"))

driver.close()
