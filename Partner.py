
class partner():

    def __init__(self,driver):
        self.driver=driver
        self.partner_id='groupNode_partner_management_0'
        self.buss_id='itemNode_SalesBusinessPlans_6' #id="itemNode_SalesBusinessPlans_6"


    def click_partner(self):
        self.driver.find_element_by_id(self.partner_id).click()

    def click_buss_id(self):
        self.driver.find_element_by_id(self.buss_id).click()
