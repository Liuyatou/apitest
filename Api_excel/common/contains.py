#coding=utf-8

import os
# 试试git更新后的效果

# 此项目的绝对地址
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # API_3
# print(base_dir)

# 测试用例地址
case_file = os.path.join(base_dir, 'data', 'pythonexcel.xlsx')
# print(case_file)

# 切换环境配置文件地址
global_file=os.path.join(base_dir,"config","global.conf")
# print(global_file)
# 线上环境地址
online_file=os.path.join(base_dir,"config","online.conf")
# print(online_file)
# 测试环境地址
test_file=os.path.join(base_dir,"config","test.conf")
# print(test_file)

# mysql的配置文件地址
mysql_file=os.path.join(base_dir,"config","mysql.conf")

# 日志的地址
log_dir=os.path.join(base_dir,"log")

# 测试用例的地址
case_dir=os.path.join(base_dir,"testcases")

# 测试报告地址
report_dir=os.path.join(base_dir,"report")