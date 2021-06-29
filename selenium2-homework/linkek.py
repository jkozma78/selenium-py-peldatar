from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999")

links = links = driver.find_elements_by_tag_name("a")

file = open("links.txt", "w")
for i in links:
    file.writelines(f'{str(i.text)} \n')

file.write(f'A linkek száma:{len(links)}')
file.close()
driver.close()
