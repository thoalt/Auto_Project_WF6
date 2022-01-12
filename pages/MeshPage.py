from base.base_page import BasePage

class MeshPage(BasePage):
    lnkMeshTab_xpath = "//a[@title='Mesh']"
    btnCreateMesh_xpath = "//input[@id='createmesh']"
    txtMeshSSID_xpath = "//input[@id='Input_SSID']"
    lbMeshSSID_xpath = "//td[@id='meshnetwork']"
    txtWPAPass_xpath = "//input[@id='Input_WPA_passphrase']"
    lbWPAPass_xpath = "//td[contains(text(),'WPA Passphrase')]"
    btnApply_xpath = "//input[@id='applynew']"

    btnJoinMesh_xpath = "//input[@onclick='JoinMesh()']"
    btnSearchMesh_xpath = "//input[@onclick='ScanNeighborSSID()']"
    btnJoinManual_xpath = "//input[@onclick='Manual()']"
    txtManuMeshSSID_xpath = "//input[@id='Input_SSID']"
    lbManuMeshSSID_xpath = "//td[@id='meshnetwork']"
    txtManuWPAPass_xpath = "//input[@id='Input_WPA_passphrase']"
    lbManuWPAPass_xpath = "//td[contains(text(),'WPA Passphrase')]"
    btnApplyJoinManu_xpath = "//input[@onclick='ApplyRepeater2G()']"

    lbScannedSSID_xpath = "//td[contains(text(),'Scanned SSID Table')]"
    btnJoinSSID_xpath = "//tbody/tr[3]/td[2]/input[1]"

    # Init method
    def __init__(self, driver):
        super().__init__(driver)

    def click_mesh_tab(self):
        self.wait_and_click_element(self.lnkMeshTab_xpath)

    def click_create_mesh(self):
        self.wait_and_click_element(self.btnCreateMesh_xpath)

    def set_mesh_SSID(self, meshSSID):
        self.wait_and_set_text_element_with_delete(self.txtMeshSSID_xpath, meshSSID)

    def get_mesh_SSID(self):
        return self.wait_and_get_attribute_element(self.txtMeshSSID_xpath, 'value')

    def set_WPA_pass(self, wpaPass):
        self.wait_and_set_text_element_with_delete(self.txtWPAPass_xpath, wpaPass)

    def click_apply(self):
        self.wait_and_click_element(self.btnApply_xpath)

    def click_join_mesh(self):
        self.wait_and_click_element(self.btnJoinMesh_xpath)

    def click_search_mesh(self):
        self.wait_and_click_element(self.btnSearchMesh_xpath)

    def click_join_SSID(self):
        self.wait_and_click_element(self.btnJoinSSID_xpath)
