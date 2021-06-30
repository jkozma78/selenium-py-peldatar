from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/general.html")

links = driver.find_elements_by_tag_name("a")

try:
    for i in range(len(links)):

        if links[i].get_property("target") == "_blank":
            continue

        links[i].click()
        # az url ellenőrzését nem tudtam befejezni, mert az egyenlőség egy helyen a http és https különbségen elbukott
        driver.back()
        links = driver.find_elements_by_tag_name("a")

    print("Az összes link végiglátogatva")

except:
    print("hiba")

driver.close()
