import pytest
from selenium import webdriver
#To avoid creting webdriver.Chrome() everytime we just created a method
#setup under fixture

@pytest.fixture
def setup():
    driver = webdriver.Chrome("E:\study\seleniumpython\chromedriver.exe")
    return driver
