from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/windowgame.html")

colorcode = driver.find_element_by_id("target_color").text


def findcolor():
    for i in range(len(driver.find_elements_by_xpath("//button"))):
        window_before = driver.window_handles[0]
        driver.find_element_by_xpath(f'//button[@id={i}]').click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        secondcolor = (driver.find_element_by_xpath("//h1").text)
        if colorcode == secondcolor:
            return i
            driver.close()
            break
        driver.close()
        driver.switch_to.window(window_before)


print(f'{findcolor()}. gomb a 100-ból')

driver.quit()
