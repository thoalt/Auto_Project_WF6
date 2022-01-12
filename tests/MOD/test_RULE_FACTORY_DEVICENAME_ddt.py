import self as self
from ddt import ddt, data, unpack, file_data
import pytest
from pages.HomePage import HomePage
from assertpy import assert_that
import softest
from utilites.handle_excel import ExcelPaser

@pytest.mark.usefixtures("login_webpage")
@ddt
class Test_RULE_FACTORY_DEVICENAME(softest.TestCase):
    excel_sheet = "RuleInputDefault"
    excel_file = ExcelPaser.open_workbook()

    @pytest.fixture(autouse=True, scope="function")
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_device_info_page()

    @data(*ExcelPaser.read_data_via_testcaseID(excel_file, excel_sheet, "RULE_FACTORY_DEVICENAME_01"))
    @unpack
    def test_RULE_FACTORY_DEVICENAME_01(self, device_name, expectResult):
        self.hp.set_device_info(deviceName=device_name, clickAction=False)
        assert_that(expectResult).contains(self.hp.get_alert_info())

    @data(*ExcelPaser.read_data_via_testcaseID(excel_file, excel_sheet, "RULE_FACTORY_DEVICENAME_02"))
    @unpack
    def test_RULE_FACTORY_DEVICENAME_02(self, device_name, expectResult):
        self.hp.set_device_info(deviceName=device_name, clickAction=False)
        assert_that(expectResult).contains(self.hp.get_alert_info())

    @data(*ExcelPaser.read_data_via_testcaseID(excel_file, excel_sheet, "RULE_FACTORY_DEVICENAME_03"))
    @unpack
    def test_RULE_FACTORY_DEVICENAME_03(self, device_name, expectResult):
        self.hp.set_device_info(deviceName=device_name, clickAction=False)
        assert_that(expectResult).contains(self.hp.get_alert_info())

    @data(*ExcelPaser.read_data_via_testcaseID(excel_file, excel_sheet, "RULE_FACTORY_DEVICENAME_04"))
    @unpack
    def test_RULE_FACTORY_DEVICENAME_04(self, device_name, expectResult):
        self.hp.set_device_info(deviceName=device_name, clickAction=False)
        assert_that(expectResult).contains(self.hp.get_alert_info())

    @data(*ExcelPaser.read_data_via_testcaseID(excel_file, excel_sheet, "RULE_FACTORY_DEVICENAME_05"))
    @unpack
    def test_RULE_FACTORY_DEVICENAME_05(self, device_name, expectResult):
        self.hp.set_device_info(deviceName=device_name, clickAction=False)
        assert_that(expectResult).contains(self.hp.get_alert_info())

    @data(*ExcelPaser.read_data_via_testcaseID(excel_file, excel_sheet, "RULE_FACTORY_DEVICENAME_06"))
    @unpack
    def test_RULE_FACTORY_DEVICENAME_06(self, device_name, expectResult):
        self.hp.set_device_info(deviceName=device_name, clickAction=False)
        assert_that(self.hp.get_alert_info()).is_equal_to('')