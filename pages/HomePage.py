from base.base_page import BasePage


class HomePage(BasePage):
    lnkHomeTab_xpath = "//a[@id='titleHome']"
    btnEdit_xpath = "//img[@title='Detail Information' and @onclick='Showdetail(1);']"
    btnEditDevice_xpath = "//td[@class='hdContent01 hdContent01_clickable']"
    txtDeviceName_xpath = "//input[@id='INPUT_DEVICE']"
    lbDeviceName_xpath = "//td[contains(text(),'Device Name')]"
    txtDeviceLoc_xpath = "//input[@id='INPUT_LOCATION']"
    lbDeviceLoc_xpath = "//td[contains(text(),'Location')]"
    drpOperMode_xpath = "//select[@id='INPUT_OPERATION_MODE']"
    btnSave_xpath = "//input[@id='BUTTON_DEVICE_NAME_LOCATION']"

    # Init method
    def __init__(self, driver):
        super().__init__(driver)

    def click_home_tab(self):
        self.wait_and_click_element(self.lnkHomeTab_xpath)

    def click_btn_edit(self):
        self.wait_and_click_element(self.btnEdit_xpath)

    def click_btn_edit_device(self):
        self.wait_and_click_element(self.btnEditDevice_xpath)

    def set_device_name(self, deviceName):
        self.wait_and_set_text_element_with_delete(self.txtDeviceName_xpath, deviceName)

    def get_device_name(self):
        self.wait_and_get_attribute_element(self.txtDeviceName_xpath, 'value')

    def set_location(self, location):
        self.wait_and_set_text_element_with_delete(self.txtDeviceLoc_xpath, location)

    def get_location(self):
        self.wait_and_get_attribute_element(self.txtDeviceLoc_xpath, 'value')

    def select_operation_mode(self, mode):
        self.wait_and_select_item(self.drpOperMode_xpath, mode)

    def click_btn_save(self):
        self.wait_and_click_element(self.btnSave_xpath)

    def navigate_to_device_info_page(self):
        self.click_home_tab()
        self.click_btn_edit()
        self.click_btn_edit_device()

    def set_device_info(self, deviceName=None, location=None, clickAction=True):
        if deviceName is not None:
            self.set_device_name(deviceName)

        if location is not None:
            self.set_location(location)

        if clickAction == True:
            self.click_btn_save()

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)