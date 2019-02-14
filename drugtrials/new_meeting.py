# -*- coding: utf-8 -*-
#
# import requests
# from lxml import etree
# from mysql_pool import OPMysql
#
#
# url = 'http://jzjs2015.medmeeting.org/Content/28475'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
#     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', }
# req = requests.get(url=url,headers=headers).content
#
# response = etree.HTML(req)
#
# all_trs = response.xpath('/html/body/div[2]/div[3]/div[1]/div['
#                        '2]/div/table/tbody/tr[position()>2]')
# xuezu = ''
# time = ''
# master = ''
# role = ''
# date = response.xpath('/html/body/div[2]/div[3]/div[1]/div['
#                       '2]/div/table/tbody/tr[2]/td/p/span/text()')[0]
# for tr in all_trs:
#
#     if tr.xpath('./td/p[@align="center"]//span/text()'):
#         contents = tr.xpath('./td/p[@align="center"]//span/text()')
#         try:
#             master = contents[1]
#         except:
#             master = ''
#
#         try:
#
#
#
#         try:
#             time = contents[0].split(' ')[0]
#         except:
#             time = contents[0].split('\r\n')[0]
#         xuezu = ''.join(contents).strip()

    # if u'时间' in tr.xpath('./td/span/text()'):
    #
    #     continue
    # process_time = tr.xpath('./td[2]/span/text()')[0]
    # type = tr.xpath('./td[3]/span/text()')[0]
    # title= tr.xpath('./td[4]/span/text()')[0]
    # speaker = tr.xpath('./td[5]/span/text()')
    # if u'主持' in speaker or u'主席' in speaker:
    #     role = 0
    # if u'讲者' in speaker:
    #     role = 1
    # if u'讨论' in speaker:
    #     role = 2
    # if u'翻译' in speaker:
    #     role = 3
    # if u'评委' in speaker:
    #     role = 4
    # date = date
    # print role
