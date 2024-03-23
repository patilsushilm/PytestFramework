import time

from selenium.webdriver.common.by import By

from vtigercommonactions.common_actions import common_actions


class login_page(common_actions):

    elm_username = (By.XPATH,"//input[@name='user_name']")
    elm_password = (By.XPATH, "//input[@name='user_password']")
    elm_login = (By.XPATH, "//input[@name='Login']")
    elm_theme = (By.XPATH,"//select[@name='login_theme']")
    elm_error_msg = (By.XPATH,"//*[contains(text(),'You must specify a valid username and password.')]")
    elm_logo = (By.XPATH,"//img[@src='include/images/vtiger-crm123.gif']")
    elm_customer_portal = (By.LINK_TEXT, "vtiger Customer Portal")
    elm_tab_login = (By.ID, "login")



    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):

          self.enter_text(self.elm_username,username)
          self.enter_text(self.elm_password, password)
          self.click_element(self.elm_login)

    def login(self, username, password,theme):
          self.enter_text(self.elm_username,username)
          self.enter_text(self.elm_password, password)
          self.select_text_by_text(self.elm_theme, theme)
          self.click_element(self.elm_login)


    def verify_error_msg(self):
          return self.element_exist(self.elm_error_msg)

    def verify_logo(self):
          return self.element_exist(self.elm_logo)

    def click_customer_portal(self):
          self.click_element(self.elm_customer_portal)
          time.sleep(4)

    def handle_new_tab(self):
        loginpage = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            print(handle)
            if handle != loginpage:
                newtab = handle

        self.driver.switch_to.window(newtab)
        self.click_element(self.elm_tab_login)
        self.driver.close()
        self.driver.switch_to.window(loginpage)





