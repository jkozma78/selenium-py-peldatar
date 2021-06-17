from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
elementid = input("Keresett elem azonosítója:")

def unknown_id(id):
    driver = webdriver.Edge("D:\edge\msedgedriver")
    driver.get("http://www.python.org")
    try:
        text = driver.find_element_by_id(id).text
        return text
    except NoSuchElementException:
        return "Nem található ilyen elem"
    driver.close()

print(unknown_id(elementid))