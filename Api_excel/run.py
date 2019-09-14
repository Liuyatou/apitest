

import unittest

from Api_excel.common import HTMLTestRunnerNew
from Api_excel.common import contains

discover = unittest.defaultTestLoader.discover(contains.case_dir, "test_*.py")

with open(contains.report_dir + '/report.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            title="Python 测试用例报告",
                                            description="前程贷登录接口测试",
                                            tester="Rola.yang"
    )

    runner.run(discover)