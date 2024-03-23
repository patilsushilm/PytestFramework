from selenium.webdriver.common.by import By

from vtigercommonactions.common_actions import common_actions


class lead_page(common_actions):

    elm_new_lead = (By.LINK_TEXT,"New Lead")
    elm_save = (By.NAME, "button")
    elm_lastname = (By.NAME, "lastname")
    elm_company = (By.NAME, "company")



    def __init__(self, driver):
        super().__init__(driver)

    def create_lead(self, lname, comp):
        self.enter_last_name(lname)
        self.enter_company(comp)
        self.click_save()




    def enter_last_name(self,lname):
        self.enter_text(self.elm_lastname, lname)

    def enter_company(self,comp):
        self.enter_text(self.elm_company, comp)

    def click_save(self):
          self.click_element(self.elm_save)

    def click_new_lead(self):
          self.click_element(self.elm_new_lead)




