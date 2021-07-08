from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get("http://localhost:9999/pagination.html")

firstnames = {}

nextbutton = driver.find_element_by_id("next")

while True:
    size = len(driver.find_elements_by_xpath("//tbody/tr"))
    for i in range(size):
        ident = driver.find_element_by_xpath(f'//tbody/tr[{i + 1}]/td[1]').text
        name = driver.find_element_by_xpath(f'//tbody/tr[{i + 1}]/td[2]').text
        if re.search(r"\bA\w+", name):
            firstnames.update({ident: name})
    if nextbutton.is_enabled():
        nextbutton.click()
    else:
        break

with open("names.csv", "w") as csvfile:
    csvfile.write(str(firstnames))
driver.close()
