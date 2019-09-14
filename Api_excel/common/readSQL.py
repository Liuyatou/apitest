

import configparser
from Api_excel.common import contains

class ReadSql:

    config=configparser.ConfigParser()
    config.read(contains.mysql_file)
    host = config.get("database", "host")
    user = config.get("database", "user")
    password = config.get("database", "password")
    port = int(config.get("database", "port"))
    charset = config.get("database", "charset")

    sql=config.get("mysql","query")
    sql1=config.get("mysql","query1")
    # db=config.get("db","db")
