


import re
from Api_excel.common.config import config
import configparser

class Context:

    loan_id=None

def replace(data):
    p="#(.*?)#"  # 正则表达式
    while re.search(p,data):# 从任意位置开始查找，查到第一个就返回match object 没有找到就None
        m=re.search(p,data)
        g=m.group(1)    # 拿到参数化的key 比如loan_id
        try:
            v=config.get("data",g)   # 根据Key取值
        except configparser.NoOptionError as e:
            if hasattr(Context,g):
                v=getattr(Context,g)
            else:
                print("没找到")
                raise e


        print(v)
        data=re.sub(p,v,data,count=1)
        print(data)
    return data



