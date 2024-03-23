import time

from selenium.webdriver.common.by import By

from vtigercommonactions.common_actions import common_actions


class account_page(common_actions):

    elm_new_account = (By.LINK_TEXT,"New Account")
    elm_change = (By.NAME, "btn1")
    elm_vtiger = (By.LINK_TEXT, "vtiger")
    elm_change_text = (By.NAME, "account_name")



    def __init__(self, driver):
        super().__init__(driver)

    def click_new_Account(self):
          self.click_element(self.elm_new_account)

    def click_change_button(self):
          self.click_element(self.elm_change)
          time.sleep(3)

    def change_account(self):
        accounpage = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            print(handle)
            if handle != accounpage:
                child_page = handle

        self.driver.switch_to.window(child_page)
        self.click_element(self.elm_vtiger)
        self.driver.switch_to.window(accounpage)
        return self.get_textbox_text(self.elm_change_text,"value")








