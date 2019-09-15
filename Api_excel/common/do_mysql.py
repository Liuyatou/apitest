
#coding=utf-8

import pymysql
from Api_excel.common.readSQL import ReadSql

class Domysql:

    def __init__(self,host=ReadSql.host,
                 user=ReadSql.user,
                 password=ReadSql.password,
                 port=ReadSql.port,
                 charset=ReadSql.charset
                 ):
        self.host=host
        self.user=user
        self.password=password
        self.port=port
        self.charset=charset


    def open(self):
        # 创建数据库连接，分别指定主机，用户，密码和数据库名，保持用户有权限连接
        self.db=pymysql.connect(    host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    port=self.port,
                                    charset=self.charset

                                )

        self.cursor=self.db.cursor(pymysql.cursors.DictCursor)

    def fetchone(self,sql):
        try:
            self.open()
            self.cursor.execute(sql)
            self.db.commit()
            result=self.cursor.fetchone()
            # print("哈哈哈这是fetchone")
            return result
        except:
            print("没查到")

    def fetchall(self,sql):
        try:
            self.open()
            self.cursor.execute(sql)
            result=self.cursor.fetchall()
            print("哈哈哈哈哈fetchall")
            return result

        except:
            print("没查到")
    def close(self):
        self.cursor.close()
        self.db.close()
# if __name__ == '__main__':
#     mysql=Domysql()
#     sql=ReadSql.sql
#     mysql.fetchone(sql)
    # print(sql)

