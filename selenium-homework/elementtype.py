from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/trickyelements.html")
    element = driver.find_elements_by_xpath("//button[contains(@id, 'element')]")
    element[0].click()
    assert f'{element[0].text} was clicked' == driver.find_element_by_id("result").text

except IndexError:
    print("Nem található button type element")

finally:
    driver.close()
