class LoginPage:
    textbox_username_id = "Username"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@class = 'button-1 login-button']"
    button_logout_text = "//span[text()='Log out']"

    #from line number 2 to 5 is locators

    # here driver comes from actual test case

    def __int__(self,driver):
        self.driver = driver

    #above for initiate the local driver and self.driver is related to the class variable

    def setusername(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).cear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

# line 15 and 16 self.textbox_username_id,self is used to access the textbox_username_id

    def setpassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.button_logout_linktext).click()

# line 14 to 25 are action method to use above element(loators)

