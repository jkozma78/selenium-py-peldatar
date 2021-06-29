from selenium import webdriver

driver = webdriver.Edge("D:\\edge\\msedgedriver.exe")
driver.get("http://localhost:9999/kitchensink.html")


def print_names(lista):
    for l in lista:
        for i in l:
            print(i.text)


my_list = [driver.find_elements_by_id("carselect"), driver.find_elements_by_name("cars"),
           driver.find_elements_by_xpath("//legend")]

print_names(my_list)

driver.close()
