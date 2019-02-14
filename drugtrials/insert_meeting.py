# -*- coding: utf-8 -*-
import xlrd
import pymysql
import requests
from lxml import etree
from mysql_pool import OPMysql
sql_clint = pymysql.connect(
            host= 'rm-2ze0233bsklz6e9p7o.mysql.rds.aliyuncs.com',
            user= 'mdm_ods_operator',
            passwd= 'mdm_ods_Nx_2018',
            db= 'mdm_db_ods',
            port= 3306,
            charset= 'utf8mb4')

cursor = sql_clint.cursor()
data = xlrd.open_workbook(r'/Users/admin/Desktop/大扶康年会数据抓取_20181112.xlsx') # 打开xls文件
url_list = []
for table in data.sheets():
    nrows = table.nrows      # 获取表的行数
    for i in range(nrows):   # 循环逐行打印
        if i == 0: # 跳过第一行
            continue
        item={}
        # dates=str(table.row_values(i)[2]).replace('/','-') #年月日
        # meeting_name=table.row_values(i)[0]     #会议全程时间
        # url=table.row_values(i)[1]      #会议进程时间
        # times=table.row_values(i)[3]
        #
        # process_time=table.row_values(i)[4]     #标题内容
        # title=table.row_values(i)[5]     #讲者
        # types=table.row_values(i)[10]     #主持人
        # speaker = table.row_values(i)[7]
        # master= table.row_values(i)[6]
        # #speaker_unit = table.row_values(i)[8]
        #
        # role = str(table.row_values(i)[8]).replace('.0','')
        # xuezu = table.row_values(i)[9]
        # gather_method = 1
        # remark = '诺和'.decode('utf-8')

        name = table.row_values(i)[0]
        url = table.row_values(i)[1]

        if url.startswith('http://www.medmeeting.org/Home/Program/'):
            sql = 'select url from annual_meeting where url=%s'
            params = (url)

        # sql ="INSERT INTO annual_meeting(xuezu,date,meeting_name,url," \
        #      "time,type,process_time,title,speaker,master,remark,role,gather_method) VALUES('%s'," \
        #      "'%s','%s','%s','%s','%s'," \
        #      "'%s'," \
        #      "'%s'," \
        #      "'%s'," \
        #      "'%s','%s'," \
        #      "'%s','%s')"\
        #      % (xuezu,dates,meeting_name,url,times,types,process_time,title,speaker,master,
        #         remark,role,gather_method)
            result = cursor.execute(sql,params)
            sql_clint.commit()
            
            if  not result:
                task_item = {
                            'name': name,
                            'url': url,        
                            'type': '大扶康'
                            }
                url_list.append(task_item)
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
                if '评委' in role_name:
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
                        ppt = 'http://www.medmeeting.org' + \
                              info.xpath('./td[7]/a[1]/@href')[0]
                    except:
                        ppt = ''
                    try:
                        video = 'http://www.medmeeting.org' + info.xpath('./td['
                                                                         '7]/a['
                                                                         '2]/@href')[
                            0]
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
                try:
                    OPMysql.op_insert(OPMysql(), sql, params)
                    OPMysql.dispose(OPMysql())
                except:
                    OPMysql.op_insert(OPMysql(), sql, params)
                    OPMysql.dispose(OPMysql())