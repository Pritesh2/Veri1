from selenium import webdriver
import time
import unittest
from LoginPage import LoginPage1
from Partner import partner

class login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/Pritesh.Gethewale/PycharmProjects/pythonProject/chromedriver.exe')

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver
        driver.get('https://ccpa-test.fa.us6.oraclecloud.com/fscmUI/faces/FuseWelcome?')

        login_obj=LoginPage1(driver)

        login_obj.enter_userid('Partner.FinanceAdmin@veritas.com')
        login_obj.enter_password('Welcome1')
        login_obj.click_submit()
        time.sleep(3)
        # Partner page
        partner_obj=partner(driver)
        partner_obj.click_partner()
        time.sleep(5)
        partner_obj.click_buss_id()
        print('Business clicked')
        time.sleep(10)
        

        #print(self.driver.title)
        #self.driver.find_element_by_name('userid').send_keys('Partner.FinanceAdmin@veritas.com')
        #self.driver.find_element_by_name('password').send_keys('Welcome1')
        #self.driver.find_element_by_id('btnActive').click()

        #self.sleep(5)

        #self.driver.find_element_by_id('').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

#driver=webdriver.Chrome(executable_path='C:/Users/Pritesh.Gethewale/PycharmProjects/pythonProject/chromedriver.exe')

#driver.implicitly_wait(10)
#driver.maximize_window()


#driver.find_element_by_name('userid').send_keys('Pritesh.Gethewale@veritas.com')
#driver.find_element_by_name('password').send_keys('Welcome123')
#driver.find_element_by_id('btnActive').click()





#driver.close()

if __name__=='__main__':
    unittest.main()
