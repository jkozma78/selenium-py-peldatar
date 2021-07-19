# 011 Feladat: selenium táblázatok gyakorlása
# A feladatokat külön python fileban oldd meg.
# Minden feladat tartalmazza az elvárt filenevet. Ezen a néven fogadható el a megoldás.
# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/editable-table.html oldalt.
# A megjelenő táblázatban az alábbi feladatokat kell végrehajtanod:
# a) Addj hozzá még két teljsen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.
# b) Ellenőrizd a kereső funkciót.
# c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.
# A megoldást egy edittable.py nevű fileban kell beadnod.

import datetime
import time

from selenium import webdriver

item1 = (('Lenovo', 129.2, 11, 'Laptop'), ('Acer', 130, 23, 'Laptop'))
item2 = (('Lenovo', 119.2, 20, 'Computer'), ('Acer', 140, 23, 'Computer'))
driver = webdriver.Chrome()
driver.get("http://localhost:9999/editable-table.html")


def additems(data, method):
    for i in range(len(data)):
        if method == 'add':
            driver.find_element_by_class_name("btn.btn-success.pull-right").click()

        lastrow = (len(driver.find_elements_by_xpath('//table/tbody/tr')))

        for j in range(len(data[i])):
            cell = driver.find_element_by_xpath(f'//table/tbody/tr[{lastrow}]/td[{j + 1}]/input')
            cell.clear()
            cell.send_keys(str(data[i][j]))


additems(item1, 'add')
time.sleep(5)
additems(item2, 'modify')

driver.find_element_by_xpath('//input[@placeholder="Search..."]').send_keys('h')
finds = driver.find_elements_by_xpath('//input[@name="name"]')
for i in finds:
    print(i.get_attribute('value'))
    if 'h' not in i.get_attribute('value'):
        print("Hiba")
