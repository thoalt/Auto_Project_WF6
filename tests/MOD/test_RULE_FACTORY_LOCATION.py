import self as self
from ddt import ddt, data, unpack, file_data
import pytest
from pages.HomePage import HomePage
from assertpy import assert_that
import softest
from utilites.handle_excel import ExcelPaser

@pytest.mark.usefixtures("login_webpage")
@ddt
class Test_RULE_FACTORY_LOCATION(softest.TestCase):
    excel_sheet = "RuleInputDefault"

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_device_info_page()

    @data(*ExcelPaser.read_data_via_testcaseID(excel_sheet, "RULE_FACTORY_LOCATION_01"))
    @unpack
    def test_RULE_FACTORY_LOCATION_01(self, location, expectResult):
        self.hp.set_device_info(location=location, clickAction=False)
        assert_that(expectResult).contains(self.hp.get_alert_info())


    @data(*ExcelPaser.read_data_via_testcaseID(excel_sheet, "RULE_FACTORY_LOCATION_02"))
    @unpack
    def test_RULE_FACTORY_LOCATION_02(self, location, expectResult):
        self.hp.set_device_info(location=location, clickAction=False)
        assert_that(expectResult).contains(self.hp.get_alert_info())

    @data(*ExcelPaser.read_data_via_testcaseID(excel_sheet, "RULE_FACTORY_LOCATION_03"))
    @unpack
    def test_RULE_FACTORY_LOCATION_03(self, location, expectResult):
        self.hp.set_device_info(location=location, clickAction=False)
        assert_that(expectResult).contains(self.hp.get_alert_info())

    @data(*ExcelPaser.read_data_via_testcaseID(excel_sheet, "RULE_FACTORY_LOCATION_04"))
    @unpack
    def test_RULE_FACTORY_LOCATION_04(self, location, expectResult):
        self.hp.set_device_info(location=location, clickAction=False)
        assert_that(expectResult).contains(self.hp.get_alert_info())

    @data(*ExcelPaser.read_data_via_testcaseID(excel_sheet, "RULE_FACTORY_LOCATION_05"))
    @unpack
    def test_RULE_FACTORY_LOCATION_05(self, location, expectResult):
        self.hp.set_device_info(location=location, clickAction=False)
        assert_that(expectResult).contains(self.hp.get_alert_info())

    @data(*ExcelPaser.read_data_via_testcaseID(excel_sheet, "RULE_FACTORY_LOCATION_06"))
    @unpack
    def test_RULE_FACTORY_LOCATION_06(self, location, expectResult):
        self.hp.set_device_info(location=location, clickAction=False)
        assert_that(self.hp.get_alert_info()).is_equal_to('')