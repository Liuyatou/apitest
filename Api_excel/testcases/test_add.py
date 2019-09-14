

import unittest
from Api_excel.common import http_request
from Api_excel.common import do_excle
from Api_excel.common import do_mysql
from Api_excel.common import contains
from Api_excel.common.readSQL import ReadSql
from ddt import ddt,data
from Api_excel.common import context

@ddt
class TestAdd(unittest.TestCase):

    excel=do_excle.DoExcel(contains.case_file,"add")
    cases=excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request=http_request.HttpRequest_Session()

    @data(*cases)
    def test_add(self,case):
        # 在请求之前替换参数化的值
        case.data = context.replace(case.data)
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(str(case.expected), resp.json()['code'])
            self.excel.write_excel(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.excel.write_excel(case.case_id + 1, resp.text, 'FAIL')
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()



