import time

import pytest

from conftest import BaseUrl, ExcelPath, SheetName
from vtigercommonactions.common_actions import common_actions
from vtigerpages.account_page import account_page
from vtigerpages.home_page import home_page
from vtigerpages.lead_page import lead_page
from vtigerpages.login_page import login_page
from vtigerpages.vendor_page import vendor_page


@pytest.mark.usefixtures("browser_setup")
class Test_login:

    def setup_class(self):
        self.driver.get(BaseUrl)

        data = common_actions(self.driver)
        self.dt = data.readExcel(ExcelPath, SheetName)
        self.lp = login_page(self.driver)
        self.hp = home_page(self.driver)
        self.ldp = lead_page(self.driver)
        self.vnd = vendor_page(self.driver)
        self.ap = account_page(self.driver)


    def test_verify_logo(self):
        print(self.dt)
        print("logo is displaying",self.lp.verify_logo())
        assert True , self.lp.verify_logo()



    # def test_invalid_login_TC01(self):
    #     self.lp.login("admin1","1234","orange")
    #     assert self.lp.verify_error_msg(),True



    def test_valid_login_TC02(self):
        self.lp.login(self.dt.get("TC01").get("Userid"),self.dt.get("TC01").get("Password"),"nature")
        print("logout is displaying", self.hp.verify_logout())
        assert True,self.hp.verify_logout()




    # def test_create_lead_wit_mandadoty_fields(self):
    #     self.ldp.click_new_lead()
    #     self.ldp.click_save()
    #     time.sleep(1)
    #     lnamemsg = self.ldp.get_alert_text()
    #     self.ldp.alert_accept()
    #     self.ldp.enter_last_name(self.dt.get("TC01").get("LastName"))
    #     self.ldp.click_save()
    #     time.sleep(1)
    #     compmsg = self.ldp.get_alert_text()
    #     self.ldp.alert_accept()
    #     self.ldp.enter_company(self.dt.get("TC01").get("Company"))
    #     self.ldp.click_save()
    #     assert lnamemsg, "Last Name cannot be empty"
    #     assert compmsg, "Company cannot be empty"
        #self.hp.click_logout()

    # def test_new_vendor(self):
    #     self.hp.move_mouse_arrow_menu()
    #     self.hp.click_New_Vendor()
    #     assert self.vnd.verify_vendor(), True


    # def test_drang_drop(self):
    #     self.hp.click_my_account()
    #     self.hp.click_customise()
    #     self.hp.perform_drag_drop()
    #     assert self.hp.get_text_dest(), "Activities"

    #
    # def test_handle_account_pop_window(self):
    #     self.ap.click_new_Account()
    #     self.ap.click_change_button()
    #     assert self.ap.change_account(), "vtiger"

    # def test_handle_account_pop_window(self):
    #     self.lp.click_customer_portal()
    #     self.lp.handle_new_tab()
    #     assert self.lp.verify_logo(),True







