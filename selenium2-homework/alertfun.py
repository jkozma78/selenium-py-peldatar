import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://localhost:9999/alert_playground.html")

alertnames = ("alert", "confirmation", "prompt")


def double_click():
    alert = driver.find_element_by_id("double-click")
    ActionChains(driver).double_click(alert).perform()
    alertbox = driver.switch_to.alert
    assert alertbox.text == "You double clicked me!!!, You got to be kidding me"
    alertbox.accept()


def click_alert(alert):
    driver.find_element_by_name(alert).click()
    alertbox = driver.switch_to.alert

    if alert == "prompt":
        alertbox.send_keys("Prompt text")
        alertbox.accept()
        assert (driver.find_element_by_id("demo").text) == "You entered: Prompt text"
    else:
        alertbox.accept()


for i in alertnames:
    click_alert(i)

double_click()

driver.close()
