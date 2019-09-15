#coding=utf-8

import unittest
from ddt import ddt,data
from Api_excel.common import http_request
from Api_excel.common import do_excle
from Api_excel.common import contains
from Api_excel.common.readSQL import ReadSql
from Api_excel.common.do_mysql import Domysql
from Api_excel.common.context import Context
from Api_excel.common import context

@ddt
class TestInvest(unittest.TestCase):
    excel=do_excle.DoExcel(contains.case_file,"invest")
    cases=excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request=http_request.HttpRequest_Session()
        cls.mysql=Domysql()
        cls.readsql=ReadSql.sql1

    @data(*cases)
    def test_invest(self,case):
        print("开始执行测试",case.title)

        # 获取标的的id
        # loan_id=
        # 请求之前替换参数化的值 先从Excel读取 再取值替换
        case.data=context.replace(case.data)
        resp=self.http_request.request(case.method,case.url,case.data)

        try:
            self.assertEqual(str(case.expected), resp.json()['code'])
            self.excel.write_excel(case.case_id + 1, resp.text, 'PASS')

            # 判断加标成功之后，去数据库查询，取到loan_id
            if resp.json()["msg"]=="加标成功":
                loan_id=self.mysql.fetchone(self.readsql)[0]
                print("标的id:",loan_id)
                # 把loan_id保存到类属性里面
                setattr(Context,"loan_id",str(loan_id))

        except AssertionError as e:
            self.excel.write_excel(case.case_id + 1, resp.text, 'FAIL')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()