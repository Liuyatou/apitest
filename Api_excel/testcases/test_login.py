


import unittest
from Api_excel.common import http_request
from Api_excel.common import do_excle
from Api_excel.common import contains
from Api_excel.common import logger
from ddt import ddt,data

logger=logger.get_logger(__name__)
@ddt
class TestLogin(unittest.TestCase):
    # 打开excel表格
    excel = do_excle.DoExcel(contains.case_file, "login")
    # 获取case列表  放cases实例
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.info("准备测试前置")
        cls.http_request=http_request.HttpRequest_Session()

    @data(*cases)
    def test_login(self,case):
            logger.info("开始测试：{0}".format(case.title))
            resp=self.http_request.request(case.method,case.url,case.data)
            try:
                self.assertEqual(case.expected,resp.text)
                self.excel.write_excel(case.case_id+1,resp.text,"PASS")
            except AssertionError as e:
                self.excel.write_excel(case.case_id+1,resp.text,"FAIL")
                logger.error("报错了：{0}".format(case.title))
                raise e
                logger.info("结束测试：{0}".format(case.title))
    @classmethod
    def tearDownClass(cls):
        logger.info("测试后置处理")
        cls.http_request.close()



