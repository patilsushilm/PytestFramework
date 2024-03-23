import time

from selenium.webdriver.common.by import By

from vtigercommonactions.common_actions import common_actions


class vendor_page(common_actions):


    elm_vendor_info = (By.XPATH, "//*[text()='Vendor Information:']")



    def __init__(self, driver):
        super().__init__(driver)





    def verify_vendor(self):
          return self.element_exist(self.elm_vendor_info)






