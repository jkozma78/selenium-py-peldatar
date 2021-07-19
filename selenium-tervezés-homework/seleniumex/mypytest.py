# seleniumex.py pytest formában
# parancssorból a pytest mypytest.py pparancs kiadása
from selenium import webdriver


class TestSuite(object):
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def teardown(self):
        self.driver.close()

    def test_first_testcase(self):
        elementid = "q"
        self.driver.find_element_by_name(elementid).text

    def test_second_testcase(self):
        elementid = "akármi"
        self.driver.find_element_by_name(elementid).text
