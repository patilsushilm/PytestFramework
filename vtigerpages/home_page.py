import time

from selenium.webdriver.common.by import By

from vtigercommonactions.common_actions import common_actions


class home_page(common_actions):

    elm_logout = (By.LINK_TEXT,"Logout")
    elm_arrow_menu = (By.ID, "showSubMenu")
    elm_new_vendor_menu = (By.LINK_TEXT, "New Vendor")
    elm_MyAccount = (By.LINK_TEXT, "My Account")
    elm_customise = (By.NAME, "Customise")
    elm_source =  (By.ID, "cl3")
    elm_dest = (By.ID, "cl9")





    def __init__(self, driver):
        super().__init__(driver)

    def click_my_account(self):
        self.click_element(self.elm_MyAccount)

    def click_customise(self):
        self.click_element(self.elm_customise)

    def perform_drag_drop(self):
        self.mouse_drag_drop(self.elm_source,self.elm_dest)

    def get_text_dest(self):
        return self.get_element_text(self.elm_dest)

    def move_mouse_arrow_menu(self):
        self.move_mouse(self.elm_arrow_menu)
        time.sleep(1)

    def click_New_Vendor(self):
        self.move_left_click(self.elm_new_vendor_menu)

    def verify_logout(self):
          return self.element_exist(self.elm_logout)

    def click_logout(self):
          self.click_element(self.elm_logout)




