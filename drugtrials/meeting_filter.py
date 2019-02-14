# -*- coding: utf-8 -*-

import requests
from lxml import etree
from mysql_pool import OPMysql

url_list = [

    {'name': '2017中华医学会放射肿瘤治疗学分会',
     'url': 'http://www.medmeeting.org/Home/Program/5128'
        , 'type': 'dra'},
    {'name': '2016中国肿瘤内科大会',
     'url': 'http://www.medmeeting.org/Home/Program/2730'
        , 'type': 'dra'},

]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', }
meeting_date = None
for strat_info in url_list:
    req = requests.get(url=strat_info['url'], headers=headers)
    html = etree.HTML(req.content)
    result_lsit = html.xpath('//*[@id="programDiv"]/div/div[@class="result"]')
    for result in result_lsit:
        all_tables = result.xpath('./*')[1:]
        for table in all_tables:

            if table.xpath('./span/text()'):
                meeting_date = table.xpath('./span/text()')[0]
                continue

            start_time = table.xpath('.//p[@class="sjbt"]/b[1]/text()')[0]
            try:
                xueshu = table.xpath('.//p[@class="sjbt"]/b[2]/text()')[0]
            except:
                xueshu = ''
            zhuchi = table.xpath('.//p[@class="zcr"]//text()')
            if zhuchi:

                master = ''.join(zhuchi).replace(
                    '\r\n', '').replace(' ', '').strip()
            else:
                zhuchi = table.xpath('.//p[@class="zhuxi"]//text()')

                master = ''.join(zhuchi).replace(
                    '\r\n', '').replace(' ', '').strip()

            info_list = table.xpath('./tbody/tr[position()>1]')
            role = ''

            try:
                role_name = table.xpath('./tbody/tr[1]/td[5]/text('
                                        ')')[0].encode('utf-8')
                if '主持' in role_name or '主席' in role_name:
                    role = 0
                if '讲者' in role_name:
                    role = 1
                if '讨论' in role_name:
                    role = 2
                if '翻译' in role_name:
                    role = 3
                if '评委' in role_name :
                    role = 4

            except BaseException:
                role = ''
            if not table.xpath('./tbody/tr'):

                start_time = table.xpath('.//p[@class="sjbt"]/b[1]/text()')[0]
                try:
                    xueshu = table.xpath('.//p[@class="sjbt"]/b[2]/text()')[0]
                except:
                    xueshu = ''
                zhuchi = ''
                master = ''
                role = ''
                time = start_time
                xuezu = xueshu
                master = master
                date = meeting_date.replace(
                    u'年', '-').replace(u'月', '-').replace(u'日', '')
                url = req.url
                meeting_name = strat_info['name']
                remark = strat_info['type']
                process_time = ''
                type = ''
                speaker = ''
                speaker_unit = ''
                title = ''
                ppt = ''
                video = ''
                gather_method = 1
                sql = "insert into annual_meeting(xuezu,date,meeting_name," \
                      "url,master,time," \
                      "process_time,type,title,role,speaker," \
                      "speaker_unit,ppt,video,remark,gather_method) values(" \
                      "%s,%s," \
                      "%s," \
                      "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
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
                    speaker_unit,
                    ppt,
                    video,
                    remark,
                    gather_method)
                OPMysql.op_insert(OPMysql(), sql, params)
                OPMysql.dispose(OPMysql())
                continue

            for info in info_list:
                if info.xpath('./td[@colspan="5"]/strong'):
                    title = ''.join(
                        info.xpath(
                            './td[@colspan="5"]/strong/text('
                            ')')).strip()
                    
                    process_time = ''
                    type = ''
                    speaker = ''
                    speaker_unit = ''

                else:

                    try:
                        process_time = info.xpath('./td[2]/text()')[
                            0].replace(
                            '\r\n', '').replace(' ', '').strip()
                    except BaseException:
                        process_time = ''
                    try:
                        type = info.xpath('./td[3]/p/text()')[0].replace(
                            '\r\n', '').replace(' ', '').strip()
                    except BaseException:
                        type = ''
                    try:
                        title = info.xpath('./td[4]/p/text()')[0]
                    except BaseException:
                        title = ''
                    try:
                        speaker = info.xpath('./td[5]/a/p/text()')[0]
                    except BaseException:
                        speaker = ''
                        role = ''
                    try:
                        speaker_unit = info.xpath('./td[6]/p/text()')[0]
                    except BaseException:
                        speaker_unit = ''
                    try:
                        ppt = 'http://www.medmeeting.org'+info.xpath('./td[7]/a[1]/@href')[0]
                    except:
                        ppt = ''
                    try:
                        video = 'http://www.medmeeting.org'+info.xpath('./td['
                                                                       '7]/a['
                                                                       '2]/@href')[0]
                    except:
                        video = ''
                
                time = start_time
                xuezu = xueshu
                master = master
                date = meeting_date.replace(
                    u'年', '-').replace(u'月', '-').replace(u'日', '')
                url = req.url
                meeting_name = strat_info['name']
                remark = strat_info['type']

                gather_method = 1
                sql = "insert into annual_meeting(xuezu,date," \
                      "meeting_name," \
                      "url,master,time," \
                      "process_time,type,title,role,speaker," \
                      "speaker_unit,ppt,video,remark,gather_method) values(" \
                      "%s,%s,%s,%s," \
                      "%s," \
                      "%s,%s,%s,%s,%s," \
                      "%s," \
                      "%s,%s,%s,%s,%s)"
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
                    speaker_unit,
                    ppt,
                    video,
                    remark,
                    gather_method)
                OPMysql.op_insert(OPMysql(), sql, params)
                OPMysql.dispose(OPMysql())
