import self as self
from ddt import ddt, data, unpack, file_data
import pytest
from pages.HomePage import HomePage
import softest
from utilites.handle_excel import ExcelPaser
from utilites.utils import Utils
import inspect


@pytest.mark.usefixtures("login_webpage")
@ddt
class Test_RULE_FACTORY_DEVICENAME(softest.TestCase):
    excel_sheet = "RuleInputDefault"
    excel_file = ExcelPaser.open_workbook()

    @pytest.fixture(autouse=True, scope="function")
    def class_setup(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_device_info_page()
        self.ut = Utils()

    def setting_device_name(self, dataLst):
        alertList = []
        for data in dataLst:
            self.hp.set_device_info(deviceName=data, clickAction=False)
            alertList.append([data, self.hp.get_alert_info()])
        return alertList

    def test_RULE_FACTORY_DEVICENAME_01(self):
        # Read data from Excel file via testcase ID
        testID = self.ut.get_testcase_id(inspect.stack()[0][3])
        dataLst, expected = ExcelPaser.read_data_via_testcaseID(self.excel_file, self.excel_sheet, testID)

        # Setting Device Name, then get Actual Result
        actualResult = self.setting_device_name(dataLst)

        # Verify Alert text with expected result
        self.ut.assert_contain_value_in_list_data(actualResult, expected)

    def test_RULE_FACTORY_DEVICENAME_02(self):
        # Read data from Excel file via testcase ID
        testID = self.ut.get_testcase_id(inspect.stack()[0][3])
        dataLst, expected = ExcelPaser.read_data_via_testcaseID(self.excel_file, self.excel_sheet, testID)

        # Setting Device Name, then get Actual Result
        actualResult = self.setting_device_name(dataLst)

        # Verify Alert text with expected result
        self.ut.assert_contain_value_in_list_data(actualResult, expected)

    def test_RULE_FACTORY_DEVICENAME_03(self):
        # Read data from Excel file via testcase ID
        testID = self.ut.get_testcase_id(inspect.stack()[0][3])
        dataLst, expected = ExcelPaser.read_data_via_testcaseID(self.excel_file, self.excel_sheet, testID)

        # Setting Device Name, then get Actual Result
        actualResult = self.setting_device_name(dataLst)

        # Verify Alert text with expected result
        self.ut.assert_contain_value_in_list_data(actualResult, expected)

    def test_RULE_FACTORY_DEVICENAME_04(self):
        # Read data from Excel file via testcase ID
        testID = self.ut.get_testcase_id(inspect.stack()[0][3])
        dataLst, expected = ExcelPaser.read_data_via_testcaseID(self.excel_file, self.excel_sheet, testID)

        # Setting Device Name, then get Actual Result
        actualResult = self.setting_device_name(dataLst)

        # Verify Alert text with expected result
        self.ut.assert_contain_value_in_list_data(actualResult, expected)

    def test_RULE_FACTORY_DEVICENAME_05(self):
        # Read data from Excel file via testcase ID
        testID = self.ut.get_testcase_id(inspect.stack()[0][3])
        dataLst, expected = ExcelPaser.read_data_via_testcaseID(self.excel_file, self.excel_sheet, testID)

        # Setting Device Name, then get Actual Result
        actualResult = self.setting_device_name(dataLst)

        # Verify Alert text with expected result
        self.ut.assert_contain_value_in_list_data(actualResult, expected)

    def test_RULE_FACTORY_DEVICENAME_06(self):
        # Read data from Excel file via testcase ID
        testID = self.ut.get_testcase_id(inspect.stack()[0][3])
        dataLst, expected = ExcelPaser.read_data_via_testcaseID(self.excel_file, self.excel_sheet, testID)

        # Setting Device Name, then get Actual Result
        actualResult = self.setting_device_name(dataLst)

        # Verify Alert text with expected result
        self.ut.assert_equal_value_in_list_data(actualResult, expected)
