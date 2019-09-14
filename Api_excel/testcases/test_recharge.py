



import unittest
from Api_excel.common import do_excle
from Api_excel.common import contains
from Api_excel.common import http_request
from ddt import ddt,data
from Api_excel.common.do_mysql import Domysql
from Api_excel.common.readSQL import ReadSql
import json

@ddt
class TestRecharge(unittest.TestCase):

    excel=do_excle.DoExcel(contains.case_file,"recharge")
    cases=excel.get_cases()

    @classmethod
    def setUpClass(cls):

        cls.http_request=http_request.HttpRequest_Session()
        cls.mysql=Domysql()


    @data(*cases)
    def test_recharge(self,case):
        print(case.title)
        # 请求之前，判断是否需要执行sql
        # if case.sql is not None:
        #     sql = eval(case.sql)["sql01"]
        #     member = self.mysql.fetchone(sql)
        #     print(member['leaveamount'])
            # before = member['leaveamount']
        resp=self.http_request.request(case.method,case.url,case.data)

        try:
            # 从excel中读取的case.excepted为int型 要转换为str
            self.assertEqual(str(case.expected),resp.json()["code"])
            self.excel.write_excel(case.case_id+1,resp.text,"PASS")

            # 请求之前，判断是否需要执行sql
            # if case.sql is not None:
            #     sql = eval(case.sql)["sql1"]
            #     member = self.mysql.fetchone(sql)
            #     print(member["leaveamount"])
            #     after = member["leaveamount"]
            #     recharge_amount = int(eval(case.data)["aomunt"])
            #     self.assertEqual(before+recharge_amount,after)
        except AssertionError as e:
            self.excel.write_excel(case.case_id,resp.text,"FAIL")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()


