# -*- coding: utf-8 -*-
import requests
from lxml import etree
from mysql_pool import OPMysql

url = 'http://3913.meeting.so/msite/program/details/cn/?&d=2018-09-09'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', }
req = requests.get(url=url,headers=headers).content

response = etree.HTML(req)
date = url.split('=')[1]
all_tables = response.xpath('//div[@class="tab-content"]')
for table in all_tables:

    time = table.xpath('./div[@class="session_time"]/text()')[1]
    xuezu = table.xpath('./div[@class="session_time"]/p/text()')[0]
    try:
        master = ''.join(table.xpath('./div[@class="zhuchi"]//text()')).strip()
    except:
        master = ''
    all_trs = table.xpath('./table/tbody/tr')

    for tr in all_trs:
        
        time = time
        xuezu = xuezu
        date = date
        try:
            process_time = tr.xpath('./td[1]/text()')[0]
        except:
            process_time = ''
        try:
            type = tr.xpath('./td[2]/text()')[0]
        except:
            type = ''
        try:
            title = tr.xpath('./td[3]/text()')[0].strip()
        except:
            title = ''
        try:
            speaker = tr.xpath('./td[4]/a/text()')[0]
        except:
            speaker = ''
        master = master
        role = 1
        remark = '诺和'
        gather_method = 1

        meeting_name = '中华医学会第二十次全国心血管年会暨第十二届钱江国际心血管病会议（2018）'

        sql = "insert into annual_meeting(xuezu,date," \
              "meeting_name," \
              "url,master,time," \
              "process_time,type,title,role,speaker," \
              "remark,gather_method) values(" \
              "%s,%s,%s,%s," \
              "%s," \
              "%s,%s,%s,%s,%s," \
              "%s," \
              "%s,%s)"
        params = (
            xuezu,
            date,
            meeting_name,
            url,
            master,
            time,
            process_time,
            type,
            title,
            role,
            speaker,
            remark,
            gather_method)
        OPMysql.op_insert(OPMysql(), sql, params)
        OPMysql.dispose(OPMysql())

