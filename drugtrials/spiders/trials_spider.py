# -*- coding: utf-8 -*-
import scrapy
from drugtrials import settings
from drugtrials.items import DrugtrialsItem, DrugItem, Indicators, ResearchInfo, \
    EthicsCommittee,ResearcherItem
import sys,time

reload(sys)
sys.setdefaultencoding('utf-8')


class DrugtrialsSpiderSpider(scrapy.Spider):
    name = 'trials_spider'
    allowed_domains = ['chinadrugtrials']
    url = 'http://www.chinadrugtrials.org.cn/eap/clinicaltrials.searchlist'

    def start_requests(self):

        data = {

            'rule': 'CTR',
            'currentpage': '',
            'pagesize': '20',
            'keywords': '',
            'reg_no': 'CTR'
        }

        data['currentpage'] = '1'
        data_list = [{
        'keywords': '乳腺癌'},
        {'keywords': 'CDK4'},{'keywords':'Abemaciclib'},
        {'keywords': 'Verzenio'},{'keywords': 'palbociclib'},{'keywords':
        'CDK6'},{'keywords': '曲妥珠单抗'}
        ]
        for data in data_list:
            yield scrapy.FormRequest(
                url=self.url,
                formdata=data,
                callback=self.parse_info,
                dont_filter=True,
                meta={'data':data}

            )

    def parse_info(self, response):

        data = response.meta['data']
        start_data = {

            'rule': 'CTR',
            'currentpage': '',
            'pagesize': '20',
            'keywords': '',
            'reg_no': 'CTR'

        }
        total_pages = response.xpath('//*[@id="searchfrm"]/div/div[4]/div['
                                     '1]/a[3]/text()').extract_first()

        start_data['keywords'] = data['keywords']
        for page in range(1, int(total_pages) + 1):

            start_data['currentpage'] = str(page)
            yield scrapy.FormRequest(
                url=self.url,
                formdata=start_data,
                callback=self.parse_html,
                dont_filter=True
            )

    def parse_html(self, response):

        url = 'http://www.chinadrugtrials.org.cn/eap/clinicaltrials.searchlistdetail'
        tables = response.xpath('//*['
                                '@id="searchfrm"]/div/table/tr['
                                'position()>1]')
        data = {
            'ckm_id': '',
            'ckm_index': '',
            'sort': 'desc',
            'sort2': 'desc',
            'rule': 'CTR',
            'currentpage': '',
            'reg_no': 'CTR'
        }

        for tr in tables:

            article_id = tr.xpath('./td[last()]/a/@id').extract_first()

            data['ckm_id'] = article_id
            yield scrapy.FormRequest(
                url=url,
                formdata=data,
                callback=self.parse_article,
                dont_filter=True
            )

    def parse_article(self, response):

        item = DrugtrialsItem()
        item['first_publication_time'] = response.xpath(
            '/html/body/div/table/tbody/tr[2]/td/div[2]/div/div[2]/div['
            '1]/div[3]/table/tr[2]/td[4]/text()').extract_first().replace(
            '\r\n', '').strip()

        item['register_number'] = response.xpath('//*['
                                                 '@id="div_open_close_01"]/table['
                                                 '1]/tr[1]/td[2]/text('
                                                 ')').extract_first().replace(
            '\r\n', '').strip()

        item['adaptation_disease'] = response.xpath(
            '//*[@id="div_open_close_01"]/table['
            '1]/tr[2]/td[2]/text()').extract_first().replace('\r\n',
                                                             '').strip()

        item['Pilot_topic'] = response.xpath('//*['
                                             '@id="div_open_close_01"]/'
                                             'table[1]/tr[3]/td[2]/text('
                                             ')').extract_first().replace(
            '\r\n',
            '').strip()

        item['major_topic'] = response.xpath('//*['
                                             '@id="div_open_close_01"]'
                                             '/table[1]/tr[4]/td[2]/text('
                                             ')').extract_first().replace(
            '\r\n',
            '').strip()

        item['project_number'] = response.xpath('//*['
                                                '@id="div_open_close_01"]/table[1]'
                                                '/tr[5]/td[2]/text('
                                                ')').extract_first().replace(
            '\r\n', '').strip()

        item['Clinical_application'] = response.xpath('//*['
                                                      '@id="div_open_close_01"]/'
                                                      'table[1]/'
                                                      'tr[6]/td[2]/text('
                                                      ')').extract_first().replace(
            '\r\n', '').strip()
        try:
            item['drug_name'] = response.xpath('//*['
                                           '@id="div_open_close_01"]/'
                                           'table[1]/tr[7]/td[2]/text('
                                           ')').extract_first().replace('\r\n',
                                                                        '').strip()
        except:
            item['drug_name'] = ''

        item['drug_type'] = response.xpath('//*['
                                           '@id="div_open_close_01"]/'
                                           'table[1]/tr[8]/td[2]/text('
                                           ')').extract_first().replace('\r\n',
                                                                        '').strip()

        item['contact_name'] = response.xpath('//*['
                                              '@id="div_open_close_01"]/table['
                                              '2]/tr[2]/td[2]/text('
                                              ')').extract_first().replace(
            '\r\n',
            '').strip()
        item['contact_phone'] = response.xpath('//*['
                                               '@id="div_open_close_01"]/table['
                                               '2]/tr[3]/td[2]/text()').extract_first().replace(
            '\r\n',
            '').strip()
        item['contact_address'] = response.xpath('//*['
                                                 '@id="div_open_close_01"]/table['
                                                 '2]/tr[4]/td[2]/text()').extract_first().replace(
            '\r\n',
            '').strip()
        item['project_fund'] = response.xpath('//*['
                                              '@id="div_open_close_01"]/table['
                                              '2]/tr[5]/td[2]/text()').extract_first().replace(
            '\r\n',
            '').strip()
        item['contact_email'] = response.xpath('//*['
                                               '@id="div_open_close_01"]/table['
                                               '2]/tr[3]/td[4]/text()').extract_first().replace(
            '\r\n',
            '').strip()
        item['contact_code'] = response.xpath('//*['
                                              '@id="div_open_close_01"]/table['
                                              '2]/tr[4]/td[4]/text('
                                              ')').extract_first().replace(
            '\r\n',
            '').strip()

        item['applicant_name'] = ''
        #//*[@id="div_open_close_01"]/table[2]/tr[1]/td[2]
        #//*[@id="div_open_close_01"]/table[2]/tr[1]/td[2]/table/tr/td[2]
        applicant_names = response.xpath('//*[@id="div_open_close_01"]/table['
                                         '2]/tr[1]/td['
                                         '2]/table/tr')
        # update_time = time.localtime(int(time.time()))
        # item['update_time'] = time.strftime(
        #     "%Y-%m-%d %H:%M:%S", update_time)

        if applicant_names:
            for applicant_name in applicant_names:
                item['applicant_name'] += applicant_name.xpath(
                    './td[2]/text()').extract_first(
                ).replace(
                    '\r\n',
                    '').strip() + '\n'


        else:
            item['applicant_name'] = response.xpath('//*['
                                                    '@id="div_open_close_01"]/table[2]/tr[1]/td[2]/text()').extract()[0].replace(
                    '\r\n',
                    '').strip()

        item['study_goal'] = response.xpath(
            '//*[@id="div_open_close_01"]/table['
            '3]/tr[2]/td/text()').extract_first().replace('\r\n',
                                                          '').strip()
        item['study_class'] = response.xpath('//*['
                                             '@id="div_open_close_01"]/table['
                                             '3]/tr[4]/td/table/tr[1]/td[3]/text()').extract_first().replace(
            '\r\n',
            '').strip()
        item['study_fenqi'] = response.xpath('//*['
                                             '@id="div_open_close_01"]/table['
                                             '3]/tr[4]/td/table/tr[2]/td[3]/text()').extract_first().replace(
            '\r\n',
            '').strip()
        item['study_type'] = response.xpath('//*['
                                            '@id="div_open_close_01"]/table['
                                            '3]/tr[4]/td/table/tr['
                                            '3]/td[3]/text()').extract_first().replace(
            '\r\n',
            '').strip()
        item['study_random'] = response.xpath('//*['
                                              '@id="div_open_close_01"]/table['
                                              '3]/tr[4]/td/table/tr[4]/td[3]/text()').extract_first().replace(
            '\r\n',
            '').strip()

        item['study_blinding'] = response.xpath('//*['
                                                '@id="div_open_close_01"]/table['
                                                '3]/tr[4]/td/table/tr['
                                                '5]/td[3]/text()').extract_first().replace(
            '\r\n',
            '').strip()
        item['study_range'] = response.xpath('//*['
                                             '@id="div_open_close_01"]/table['
                                             '3]/tr[4]/td/table/tr['
                                             '6]/td[3]/text()').extract_first().replace(
            '\r\n',
            '').strip()
        item['accept_test_age'] = ''.join(response.xpath('//*['
                                                         '@id="div_open_close_01"]/table['
                                                         '3]/tr[6]/td[2]/text()')
                                          .extract()).replace('\r\n',
                                                              '').replace('\t',
                                                                          '').strip()

        item['accept_test_sex'] = response.xpath('//*['
                                                 '@id="div_open_close_01"]/table['
                                                 '3]/tr[7]/td[2]/text()').extract_first().replace(
            '\r\n',
            '').strip()
        # 健康测试者
        item['health_test_person'] = response.xpath('//*['
                                                    '@id="div_open_close_01"]/table['
                                                    '3]/tr[8]/td[2]/text()').extract_first().replace(
            '\r\n',
            '').strip()

        # 入选标准
        item['inclusion_criteria'] = ''

        # 排除标准
        item['exclusion_criteria'] = ''
        inclusion_tables = response.xpath('//*[@id="div_open_close_01"]/table[3]/tr[9]/td[2]/table/tr')


        for inclusion_tr in inclusion_tables:
            item['inclusion_criteria'] += inclusion_tr.xpath(
                './td[2]/text()').extract_first().replace('\r\n','').strip(

            )+'\n'



        exclusion_tables = response.xpath('//*['
                                          '@id="div_open_close_01"]/table['
                                          '3]/tr[10]/td[2]/table/tr')
        for exclusion_tr in exclusion_tables:
            item['exclusion_criteria'] += exclusion_tr.xpath(
                './td[2]/text()').extract_first().replace('\r\n',
                                                          '').strip() + '\n'

        # 目标入组人数
        item['except_person_number'] = ''.join(response.xpath('//*['
                                                              '@id="div_open_close_01"]/table[3]/tr[11]/td[2]/text()').extract()).replace(
            '\r\n',
            '').strip()
        item['actual_person_number'] = ''.join(response.xpath('//*['
                                                              '@id="div_open_close_01"]/table[3]/tr[12]/td[2]/text()').extract()).replace(
            '\r\n',
            '').strip()

        item['data_safety_regulatory'] = ''.join(response.xpath('//*['
                                                                '@id="div_open_close_01"]/table[3]/tr[19]/td/text()')
                                                 .extract()).replace('\r\n',
                                                                     '').strip()[
                                         -1:],
        item['for_test_buy_insurance'] = ''.join(response.xpath(
            '//*[@id="div_open_close_01"]/table[3]/tr[20]/td/text()')
                                                 .extract()).replace('\r\n',
                                                                     '').strip()[
                                         -1:],

        item['first_test_person_time'] = response.xpath('//*['
                                                        '@id="div_open_close_01"]/table[4]/tr/td/text()').extract_first().replace(
            '\r\n',
            '').strip()

        item['test_finish_time'] = response.xpath(
            '//*[@id="div_open_close_01"]/table[5]/tr/td/text()').extract_first().replace(
            '\r\n',
            '').strip()

        # 试验状态
        item['study_status'] = ''.join(response.xpath('//*['
                                                     '@id="div_open_close_01"]/table['
                                                     '8]/tr/td/text()').extract(
        )).replace('\r\n', '').replace('\t', '').strip()

        # ---------------------------------
        # 分表数据
        test_drug_tables = response.xpath('//*['
                                          '@id="div_open_close_01"]/table['
                                          '3]/tr[14]/td[2]/table/tr[position('
                                          ')>1]')

        for test_drug in test_drug_tables:
            drug_item = DrugItem()
            drug_item['drug_type'] = '试验药'
            drug_item['drug_name'] = test_drug.xpath(
                './td[2]/text()').extract_first().replace('\r\n', '').strip()
            drug_item['drug_directions'] = test_drug.xpath(
                './td[3]/text()').extract_first().replace('\r\n',
                                                          '').strip()
            drug_item['register_number'] = item['register_number']
            # update_time = time.localtime(int(time.time()))
            # drug_item['update_time'] = time.strftime(
            #     "%Y-%m-%d %H:%M:%S", update_time)
            yield drug_item

        contrast_drug_tables = response.xpath('//*['
                                              '@id="div_open_close_01"]/table['
                                              '3]/tr[15]/td[2]/table/tr['
                                              'position()>1]')

        for contrast_drug in contrast_drug_tables:
            drug_item = DrugItem()
            drug_item['drug_type'] = '对照药'
            drug_item['drug_name'] = contrast_drug.xpath(
                './td[2]/text()').extract_first().replace('\r\n',
                                                          '').strip()
            drug_item['drug_directions'] = contrast_drug.xpath(
                './td[3]/text()').extract_first().replace('\r\n',
                                                          '').strip()
            drug_item['register_number'] = item['register_number']
            # update_time = time.localtime(int(time.time()))
            # drug_item['update_time'] = time.strftime(
            #     "%Y-%m-%d %H:%M:%S", update_time)
            yield drug_item

        primary_point_tables = response.xpath('//*[@id="fIndexTable"]/tr['
                                              'position()>1]')
        for primary_point in primary_point_tables:
            indicators_item = Indicators()

            indicators_item['indicators_type'] = '主要终点指标'
            indicators_item['indicators_name'] = primary_point.xpath('./td['
                                                                   '2]/text()').extract_first().replace(
                '\r\n',
                '').strip()
            indicators_item['indicators_time'] = primary_point.xpath('./td['
                                                                   '3]/text()').extract_first().replace(
                '\r\n',
                '').strip()
            indicators_item['indicators_collect'] = primary_point.xpath('./td['
                                                                   '4]/text()').extract_first().replace(
                '\r\n',
                '').strip()
            indicators_item['register_number'] = item['register_number']
            # update_time = time.localtime(int(time.time()))
            # indicators_item['update_time'] = time.strftime(
            #     "%Y-%m-%d %H:%M:%S", update_time)
            yield indicators_item

        secondary_point_tables = response.xpath('//*[@id="fIndexCyTable"]/tr['
                                                'position()>1]')
        for secondary_point in secondary_point_tables:
            indicators_item = Indicators()
            indicators_item['indicators_type'] = '次要终点指标'
            indicators_item['indicators_name'] = secondary_point.xpath('./td['
                                                                     '2]/text()').extract_first().replace(
                '\r\n',
                '').strip()
            indicators_item['indicators_time'] = secondary_point.xpath('./td['
                                                                     '3]/text()').extract_first().replace(
                '\r\n',
                '').strip()
            indicators_item['indicators_collect'] = secondary_point.xpath('./td['
                                                                     '4]/text()').extract_first().replace(
                '\r\n',
                '').strip()
            indicators_item['register_number'] = item['register_number']

        research_tables = response.xpath('//*['
                                         '@id="div_open_close_01"]/table[6]/tr[2]/td/table')
        for research_table in research_tables:
            researcher_item = ResearcherItem()
            researcher_item['register_number'] = item['register_number']
            researcher_item['research_name'] = research_table.xpath(
                './td[2]/text()').extract_first(
            ).replace('\r\n',
                      '').replace('\t', '').strip()
            researcher_item['research_title'] = research_table.xpath(
                './td[4]/text()').extract_first(
            ).replace('\r\n',
                      '').replace('\t', '').strip()
            researcher_item['research_phone'] = research_table.xpath(
                './tr[1]/td[2]/text()').extract_first(
            ).replace('\r\n',
                      '').replace('\t', '').strip()
            researcher_item['research_email'] = research_table.xpath('./tr[1]/td[4]/text()').extract_first().replace('\r\n','').replace('\t', '').strip()
            researcher_item['research_post_address'] = research_table.xpath(
                './tr[2]/td[2]/text()').extract_first(
            ).replace('\r\n',
                      '').replace('\t', '').strip()
            researcher_item['research_post_code'] = research_table.xpath(
                './tr[2]/td[4]/text('
                ')').extract_first(
            ).replace('\r\n',
                      '').replace('\t', '').strip()
            researcher_item['research_unit'] = research_table.xpath('./tr[3]/td[2]/text()').extract_first(
            ).replace('\r\n',
                      '').replace('\t', '').strip()
            yield researcher_item
            print researcher_item
            # print item['research_name'] , '----name'
            # print item['research_title'] , '----title'
            # print item['research_phone'], '----phone'
            # print item['research_email'], '----email'
            # print item['research_post_address'], '----address'
            # print item['research_post_code'], '----code'
            # print item['research_unit'], '----unit'

        all_units_tables = response.xpath('//*[@id="hspTable"]/tr[position('
                                          ')>1]')
        for unit in all_units_tables:
            researchInfo_item = ResearchInfo()


            researchInfo_item['research_unit']= unit.xpath('./td[2]/text('
                                                            ')').extract_first(

            ).replace('\r\n',
                      '').replace('\t', '').strip()
            researchInfo_item['research_name']= unit.xpath('./td[3]/text('
                                             ')').extract_first().replace(
                '\r\n',
                '').replace('\t', '').strip()
            researchInfo_item['research_country']= unit.xpath('./td[4]/text()').extract_first(

            ).replace('\r\n',
                      '').replace('\t', '').strip()
            researchInfo_item['research_province']= unit.xpath('./td[5]/text()').extract_first(

            ).replace('\r\n',
                      '').replace('\t', '').strip()
            researchInfo_item['research_city']= unit.xpath('./td[6]/text()').extract_first(

            ).replace('\r\n',
                      '').replace('\t', '').strip()

            researchInfo_item['register_number'] = item['register_number']
            # update_time = time.localtime(int(time.time()))
            # researchInfo_item['update_time'] = time.strftime(
            #     "%Y-%m-%d %H:%M:%S", update_time)
            yield researchInfo_item


        committees = response.xpath('//*[@id="div_open_close_01"]/table['
                                    '7]/tr[position()>1]')
        for committee in committees:
            committee_item = EthicsCommittee()

            committee_item['committee_name']= committee.xpath('./td[2]/text('
                                              ')').extract_first().replace(
                '\r\n',
                '').replace('\t', '').strip()
            committee_item['conclusion']= committee.xpath('./td[3]/text('
                                          ')').extract_first().replace(
                '\r\n',
                '').replace('\t', '').strip()
            committee_item['review_time']= committee.xpath('./td[4]/text('
                                           ')').extract_first().replace(
                '\r\n',
                '').replace('\t', '').strip()
            # update_time = time.localtime(int(time.time()))
            # committee_item['update_time'] = time.strftime(
            #     "%Y-%m-%d %H:%M:%S", update_time)

            committee_item['register_number'] = item['register_number']
            yield committee_item

        yield item
