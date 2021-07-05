import csv

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/another_form.html")


def fill_data(data):
    fieldnames = ["fullname", "email", "dob", "phone"]

    for k in range(len(fieldnames)):
        driver.find_element_by_id(fieldnames[k]).clear()
        driver.find_element_by_id(fieldnames[k]).send_keys(data[k])
    driver.find_element_by_id("submit").click()


with open("table_in.csv") as csvfile:
    data = csv.reader(csvfile)
    next(csvfile)
    for i in data:
        fill_data(i)

driver.find_element_by_xpath("/html/body/main/div/button").click()
driver.close()


def compare():
    path = "C:/Users/jkozm/Downloads/table.csv"
    with open('table_in.csv') as t1:
        fileone = t1.readlines()
    with open(path) as t2:
        filetwo = t2.readlines()

    assert (fileone == filetwo)


compare()
