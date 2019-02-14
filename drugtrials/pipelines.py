# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo, settings, pymysql
from items import DrugItem, DrugtrialsItem, EthicsCommittee, ResearchInfo, \
    Indicators,ResearcherItem
import csv
from scrapy.exporters import CsvItemExporter


class DrugtrialsPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient(settings.mongo_host,
                                          settings.mongo_port)
        self.collection = self.client['drug']['drug']

    def process_item(self, item, spider):
        self.collection.save(item)
        # self.collection.update_one({'source_url': item['source_url']},
        # {'$set': dict(item)}, True)
        return item


class AqiCSVPipeline(object):
    def open_spider(self, spider):
        # 创建csv文件对象
        self.f = open("/Users/admin/Desktop/drugtrials.csv", "w")
        # 创建csv文件读写对象，数据写入到参数指定的文件里
        self.csvexporter = CsvItemExporter(self.f, unicode)
        # 开始执行item数据读写
        self.csvexporter.start_exporting()

    def process_item(self, item, spider):
        # 将item写入到文件里
        self.csvexporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 结束文件读写操作
        self.csvexporter.finish_exporting()
        # 关闭文件
        self.f.close()


class mysqlpipeline(object):

    def __init__(self):
        self.client = pymysql.Connect(
            host='rm-2ze0233bsklz6e9p7o.mysql.rds.aliyuncs.com',
            port=3306,
            user='mdm_ods_operator',
            password='mdm_ods_Nx_2018',
            database='mdm_db_ods',
            charset='utf8mb4'
        )
        self.cour = self.client.cursor()

    def process_item(self, item, spider):

        if isinstance(item,DrugtrialsItem):
            sql = "insert into clinical_trial_register(" \
                  "register_number,adaptation_disease," \
                  "Pilot_topic,major_topic," \
                  "project_number,Clinical_application," \
                  "drug_name,drug_type," \
                  "applicant_name,contact_name," \
                  "contact_phone,contact_address," \
                  "project_fund,contact_email," \
                  "contact_code,study_goal," \
                  "study_class,study_fenqi," \
                  "study_type,study_random, " \
                  "study_blinding,study_range," \
                  "accept_test_age,accept_test_sex," \
                  "health_test_person,inclusion_criteria," \
                  "exclusion_criteria,except_person_number," \
                  "actual_person_number,data_safety_regulatory," \
                  "for_test_buy_insurance," \
                  "first_test_person_time,test_finish_time,study_status," \
                  "first_publication_time) values(%s,%s," \
                  "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                  "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                  "%s,%s,%s)"
            params = (
                item['register_number'],
                # 适应症
                item['adaptation_disease'],
                # 通俗题目
                item['Pilot_topic'],
                # 正式题目
                item['major_topic'],
                # 实验方案编号
                item['project_number'],
                # 临床申请受理号
                item['Clinical_application'],
                # 药物名称
                item['drug_name'],
                # 药物类型
                item['drug_type'],
                # 申办者名称
                item['applicant_name'],
                # 联系人姓名
                item['contact_name'],
                # 联系人电话
                item['contact_phone'],
                # 联系人邮政地址
                item['contact_address'],
                # 试验项目经费来源
                item['project_fund'],
                # 联系人邮箱
                item['contact_email'],
                # 联系人邮编
                item['contact_code'],

                # 试验目的
                item['study_goal'],
                # 试验设计
                item['study_class'],
                # 实验分期
                item['study_fenqi'],
                # 实验类型
                item['study_type'],
                # 随机化
                item['study_random'],
                # 盲法
                item['study_blinding'],
                # 测试范围
                item['study_range'],
                # 受试者年龄
                item['accept_test_age'],
                # 受试者性别
                item['accept_test_sex'],
                # 健康受试者
                item['health_test_person'],
                # 入选标准
                item['inclusion_criteria'],
                # 排除标准
                item['exclusion_criteria'],
                # 目标入组人数
                item['except_person_number'],
                # 实际入组人数
                item['actual_person_number'],
                # 数据安全监察委员会
                item['data_safety_regulatory'],
                # 为受试者购买试验伤害保险
                item['for_test_buy_insurance'],
                # 第一例受试者入组日期
                item['first_test_person_time'],
                # 试验终止日期
                item['test_finish_time'],

                # # 研究者姓名
                # item['research_name'],
                # # 研究者职称
                # item['research_title'],
                # # 研究者电话
                # item['research_phone'],
                # # 研究者邮箱
                # item['research_email'],
                # # 研究者邮政地址
                # item['research_post_address'],
                # # 研究者邮编
                # item['research_post_code'],
                # # 研究者单位
                # item['research_unit'],

                item['study_status'],

                item['first_publication_time']
                    )
            self.cour.execute(sql,params)
            self.client.commit()

        if isinstance(item,ResearcherItem):
            sql = 'insert into clinic_trial_researcher(register_number,' \
                  'research_name,' \
                  '' \
                  'research_title,research_phone,' \
                  'research_email,research_post_address,research_post_code,' \
                  'research_unit) values (%s,%s,%s,%s,%s,%s,%s,%s)'
            params = (
                item['register_number'],
                # 研究者姓名
                item['research_name'],
                # 研究者职称
                item['research_title'],
                # 研究者电话
                item['research_phone'],
                # 研究者邮箱
                item['research_email'],
                # 研究者邮政地址
                item['research_post_address'],
                # 研究者邮编
                item['research_post_code'],
                # 研究者单位
                item['research_unit'],
            )
            self.cour.execute(sql, params)
            self.client.commit()
        if isinstance(item, DrugItem):
            sql = "insert into clinical_trial_drug(drug_type," \
                  "drug_name," \
                  "" \
                  "drug_directions,register_number) values (" \
                  "%s,%s,%s,%s)"
            params = (
                item['drug_type'],

                item['drug_name'],

                item['drug_directions'],

                item['register_number'],


            )
            self.cour.execute(sql, params)
            self.client.commit()
        if isinstance(item, Indicators):
            sql = "insert into clinical_trial_indicators(indicators_type," \
                  "indicators_name," \
                  "indicators_time,indicators_collect," \
                  "register_number) values (%s,%s,%s,%s,%s)"
            params = (
                item['indicators_type'],

                item['indicators_name'],

                item['indicators_time'],

                item['indicators_collect'],

                item['register_number'],)
            self.cour.execute(sql, params)

        if isinstance(item, ResearchInfo):
            sql = "insert into clinical_trial_research( research_name," \
                  "research_unit ,research_country,research_province," \
                  "research_city,register_number) values(%s,%s,%s,%s,%s,%s)"

            params = (
                item['research_name'],

                item['research_unit'],

                item['research_country'],

                item['research_province'],

                item['research_city'],

                item['register_number'])

            self.cour.execute(sql, params)
            self.client.commit()

        if isinstance(item, EthicsCommittee):
            sql = "insert into clinic_trial_committee(committee_name," \
                  "conclusion,review_time,register_number) values (%s,%s,%s,%s)"

            params = (
                item['committee_name'],

                item['conclusion'],

                item['review_time'],

                item['register_number'],
            )

            self.cour.execute(sql, params)
            self.client.commit()

        return item
