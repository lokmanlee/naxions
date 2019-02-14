# -*- coding: utf-8 -*-
import pymysql
from DBUtils.PooledDB import PooledDB


mysqlInfo = {
    'host' : 'rm-2ze0233bsklz6e9p7o.mysql.rds.aliyuncs.com',
    "user": 'mdm_ods_operator',
    "passwd": 'mdm_ods_Nx_2018',
    "db": 'mdm_db_ods',
    "port": 3306,
    "charset": 'utf8mb4'
}
class OPMysql(object):

    __pool = None

    def __init__(self):
        # 构造函数，创建数据库连接、游标
        self.coon = OPMysql.getmysqlconn()
        self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)


    # 数据库连接池连接
    @staticmethod
    def getmysqlconn():
        if OPMysql.__pool is None:
            __pool = PooledDB(creator=pymysql,
                              mincached=1,
                              maxcached=20,
                              host=mysqlInfo['host'],
                              user=mysqlInfo['user'],
                              passwd=mysqlInfo['passwd'],
                              db=mysqlInfo['db'],
                              port=mysqlInfo['port'],
                              charset=mysqlInfo['charset'])

            return __pool.connection()

    # 插入\更新\删除sql
    def op_insert(self, sql,params):

        self.cur.execute(sql,params)
        self.coon.commit()


    # 查询
    def op_select(self, sql):

        self.cur.execute(sql)  # 执行sql
        select_res = self.cur.fetchall()  # 返回结果为字典

        return select_res


    #更新
    def op_update(self, sql_list):

        for sql in sql_list:
            self.cur.execute(sql['sql'],sql['params'])  # 执行sql
        self.coon.commit()


    #释放资源
    def dispose(self):
        self.coon.close()
        self.cur.close()


if __name__ == '__main__':
    #申请资源
    opm = OPMysql()


    #释放资源
    opm.dispose()