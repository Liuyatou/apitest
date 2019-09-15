#coding=utf-8

import logging

from Api_excel.common import contains


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')

    fmt = "%(asctime)s -  %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d ]"
    formatter = logging.Formatter(fmt=fmt)

    console_handler = logging.StreamHandler()  # 控制台
    # 把日志级别放到配置文件里面配置--优化
    console_handler.setLevel('DEBUG')
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(contains.log_dir + '/case.log')
    # 把日志级别放到配置文件里面配置
    file_handler.setLevel('INFO')
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


logger = get_logger('case')
logger.info('测试开始啦')
logger.error('测试报错')
logger.debug('测试数据')
logger.info('测试结束')
