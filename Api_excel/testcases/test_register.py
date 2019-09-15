#coding=utf-8

from Api_excel.common.http_request import HttpRequest_Session
from Api_excel.common import do_excle
from Api_excel.common import contains
from ddt import ddt,data
import unittest
from Api_excel.common.do_mysql import Domysql
from Api_excel.common.readSQL import ReadSql
from Api_excel.common import context

@ddt
class TestRegister(unittest.TestCase):
    excel=do_excle.DoExcel(contains.case_file,"register")
    cases=excel.get_cases()

    @classmethod
    def setUpClass(cls):

        cls.http_request=HttpRequest_Session()
        cls.mysql=Domysql()
        cls.readsql=ReadSql.sql

    @data(*cases)
    def test_register(self,case):

        if case.data.find("register_mobile")>-1:
            self.mysql.fetchone(self.readsql)
            # sql="SELECT MAX(MobilePhone) FROM future.member"
            max_phone=self.mysql.fetchone(self.readsql)[0]   # 获取最大手机号码 str
            max_phone=int(max_phone)-203 # 最大号码转为int型 再加一
            print("最大手机号：",max_phone)
            # replace方法是特换之后重新返回一个新的字符串，所以需要使用case.data重新接收
            case.data=case.data.replace("register_mobile",str(max_phone))  # 因为手机号为str 所以要转换数据类型

        resp=self.http_request.request(case.method,case.url,case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_excel(case.case_id,resp.text,"PASS")
        except AssertionError as e:
            self.excel.write_excel(case.case_id,resp.text,"FAIL")
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()


