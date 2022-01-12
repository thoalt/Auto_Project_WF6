import inspect
import logging
import softest
from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet

class Utils(softest.TestCase):
    def assert_value_in_list_ele(self, listVal, textVal):
        for val in listVal:
            self.soft_assert(self.assertEqual, val.text, textVal)
            if val.text == textVal:
                print("Test pass")
            else:
                print("Test Fail")
        self.assert_all()

    def assert_equal_value_in_list_data(self, dataInputlst, dataVal):
        msg = ''
        for dataInput in dataInputlst:
            data = dataInput[0]
            expectVal = dataInput[1]
            if expectVal != dataVal:
                msg = "Data input: %s" %(data)
            self.soft_assert(self.assertEqual, expectVal, dataVal, msg)
        self.assert_all()


    def assert_contain_value_in_list_data(self, dataInputlst, dataVal):
        msg = ''
        for dataInput in dataInputlst:
            data = dataInput[0]
            expectVal = dataInput[1]
            if dataVal not in expectVal:
                msg = "Data input: %s" %(data)
            self.soft_assert(self.assertIn, dataVal, expectVal, msg)
        self.assert_all()

    def assert_equal(self, textVal, expectVal):
        self.soft_assert(self.assertEqual, textVal, expectVal)

    def get_testcase_id(self, functionName):
        return functionName.replace('test_', '')

    @staticmethod
    def loggen(logLevel=logging.DEBUG):
        # Set class/method name from where ít called
        logger_name = inspect.stack()[1][3]

        # Create Logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        # Create console handler or file handler and set the log level
        fh = logging.FileHandler("Automation.Log", mode='a')

        # Create Formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s -%(name)s : %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

        # Add formatter to console or file handler
        fh.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(fh)
        return logger
