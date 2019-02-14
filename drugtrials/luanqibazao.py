#-*-coding:utf-8-*-
from lxml import etree
import requests

url = 'http://301res9th.medmeeting.org/Content/27568'
headers = {

    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}
req = requests.get(url=url,headers=headers).content

html = etree.HTML(req)

trs = html.xpath('//*[@id="wrap"]/table[1]/tbody/tr[position()>1]')
for tr in trs:
    item = {}
    item['date'] = '2017-08-21'
    item['process_time'] = tr.xpath('./td[1]/p[@align="center"]['
                                    '1]/span//text()')
    # item['title'] = tr.xpath('./td[2]/p1//text()')
    # item['speaker'] = tr.xpath('./td[3]/p1//text()')
    # item['speaker_unit'] = tr.xpath('./td[4]/p1//text()')
    print item