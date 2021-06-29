from selenium import webdriver

driver = webdriver.Chrome
driver.get("http://localhost:9999/todo.html")

# itt az első todo bekattintható
# todo_element = driver.find_element_by_xpath('/html/body/div/div/div/ul/li[1]/input')
# todo_element.click()

all_todo = driver.find_elements_by_xpath('//span[@class="done-false"]')
for i in all_todo:
    print(i.text)
driver.close()
