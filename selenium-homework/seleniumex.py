from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

element = input("Keresett elem azonosítója:")


def unknown_id(azon):
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    try:
        text = driver.find_element_by_id(azon).text
        return text
    except NoSuchElementException:
        return "Nem található ilyen elem"
    driver.close()


print(unknown_id(element))
