#coding=utf-8

import configparser
from Api_excel.common import contains

class ReadConfig:
    """
    完成配置文件的读取
    """

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contains.global_file)  # 先加载global
        switch = self.config.getboolean('switch', 'on')
        if switch:  # 开关打开的时候，使用online的配置
            self.config.read(contains.online_file)
        else:  # 开关关闭的时候，使用test的配置
            self.config.read(contains.test_file)



    def get(self, section, option):
        return self.config.get(section, option)


config = ReadConfig()


# if __name__ == '__main__':
#     config = ReadConfig()
#     print(config.get('api', 'pre_url'))