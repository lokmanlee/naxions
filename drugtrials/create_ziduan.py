# -*- coding: utf-8 -*-

import pymysql
weixin = [
'weixin_name',
    'weixin_number',
    'title',
    'summary',
    'publicTime',
    'read_num',
    'likeCount',
    'commentsCount',
    'url',
    'source',
    'content',
]



client = pymysql.Connect(
            host='rm-2ze0233bsklz6e9p7o.mysql.rds.aliyuncs.com',
            port=3306,
            user='mdm_ods_operator',
            password='mdm_ods_Nx_2018',
            database='mdm_db_ods',
            charset='utf8mb4'
        )

cur = client.cursor()
for ziduan in weixin:

    sql = 'alter table source_newrank add %s varchar(512) not ' \
          'Null'%ziduan

    cur.execute(sql)
    client.commit()
