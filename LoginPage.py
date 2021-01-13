class LoginPage1():

    def __init__(self,driver):
        self.driver=driver

        self.userid='userid'
        self.password='password'
        self.login_btn='btnActive'


    def enter_userid(self,userid_name):
        self.driver.find_element_by_id(self.userid).clear()
        self.driver.find_element_by_id(self.userid).send_keys(userid_name)


    def enter_password(self,user_pass):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(user_pass)


    def click_submit(self):
        self.driver.find_element_by_id(self.login_btn).click()
