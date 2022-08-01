import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
# In Line 3 PageObjects is package LoginPage is module and LoginPage is class
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

# Here utilities.readProperties import Read Config bcz baseurl , username,password are imported form readProperties
# So this is actual communication happen between files

    logger = LogGen.loggen()
# this logger is used to send the messages to the log file

    def test_homepagetitle(self, setup):
        # self.driver = webdriver.Chrome()#replace webdriver.Chrome() with setup method,when
        #  we call the setup method will return driver

        self.logger.info("*******Test_001_login*******")
        self.logger.info("********Homepge**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Login - nopCommerce":
            assert True
            self.driver.close()
            self.logger.info("******testcase passed**********")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homepagetitle.png")
            self.driver.close()
            self.logger.info("*******test case get failed************")
            assert False


    def test_login(self, setup):
        self.logger.info("****test_case is started***********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        # here self.driver are passing as argument
        # because constructor in loginpage will automatically invoke when we
        # create an object for login page class so that constuctor is expecting driver
        # as argument and by using lp.self we are going to call the action method
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Free and open-source eCommerce platform. ASP.NET Core based shopping cart. - nopCommerce":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            assert False

# line 12 and 21 we use driver.Chrome() two times so to avoid duplication use @fixture
