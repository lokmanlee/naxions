# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DrugtrialsItem(scrapy.Item):

    update_time = scrapy.Field()
    #注册号
    register_number = scrapy.Field()
    #适应症
    adaptation_disease = scrapy.Field()
    #通俗题目
    Pilot_topic = scrapy.Field()
    #正式题目
    major_topic = scrapy.Field()
    #实验方案编号
    project_number = scrapy.Field()
    #临床申请受理号
    Clinical_application = scrapy.Field()
    # 药物名称
    drug_name = scrapy.Field()
    # 药物类型
    drug_type = scrapy.Field()
    # 申办者名称
    applicant_name = scrapy.Field()
    # 联系人姓名
    contact_name = scrapy.Field()
    #联系人电话
    contact_phone = scrapy.Field()
    #联系人邮政地址
    contact_address = scrapy.Field()
    #试验项目经费来源
    project_fund = scrapy.Field()
    #联系人邮箱
    contact_email = scrapy.Field()
    #联系人邮编
    contact_code =scrapy.Field()


    #试验目的
    study_goal = scrapy.Field()
    #试验设计
    study_class = scrapy.Field()
    #实验分期
    study_fenqi = scrapy.Field()
    #实验类型
    study_type = scrapy.Field()
    #随机化
    study_random = scrapy.Field()
    #盲法
    study_blinding = scrapy.Field()
    #测试范围
    study_range = scrapy.Field()
    #受试者年龄
    accept_test_age = scrapy.Field()
    #受试者性别
    accept_test_sex = scrapy.Field()
    #健康受试者
    health_test_person = scrapy.Field()
    #入选标准
    inclusion_criteria = scrapy.Field()
    #排除标准
    exclusion_criteria = scrapy.Field()
    #目标入组人数
    except_person_number = scrapy.Field()
    #实际入组人数
    actual_person_number = scrapy.Field()
    #数据安全监察委员会
    data_safety_regulatory = scrapy.Field()
    #为受试者购买试验伤害保险
    for_test_buy_insurance = scrapy.Field()
    # 第一例受试者入组日期
    first_test_person_time = scrapy.Field()
    # 试验终止日期
    test_finish_time = scrapy.Field()

    study_status = scrapy.Field()

    first_publication_time = scrapy.Field()

class ResearcherItem(scrapy.Item):

    register_number = scrapy.Field()
    # 研究者姓名
    research_name = scrapy.Field()
    # 研究者职称
    research_title = scrapy.Field()
    # 研究者电话
    research_phone = scrapy.Field()
    # 研究者邮箱
    research_email = scrapy.Field()
    # 研究者邮政地址
    research_post_address = scrapy.Field()
    # 研究者邮编
    research_post_code = scrapy.Field()
    # 研究者单位
    research_unit = scrapy.Field()

class DrugItem(scrapy.Item):

    update_time = scrapy.Field()
    drug_type = scrapy.Field()

    drug_name = scrapy.Field()

    drug_directions = scrapy.Field()

    register_number = scrapy.Field()

class Indicators(scrapy.Item):
    update_time = scrapy.Field()
    indicators_type = scrapy.Field()

    indicators_name = scrapy.Field()

    indicators_time = scrapy.Field()

    indicators_collect = scrapy.Field()

    register_number = scrapy.Field()

class ResearchInfo(scrapy.Item):
    update_time = scrapy.Field()
    research_name = scrapy.Field()

    research_unit = scrapy.Field()

    research_country = scrapy.Field()

    research_province = scrapy.Field()

    research_city = scrapy.Field()

    register_number = scrapy.Field()

class EthicsCommittee(scrapy.Item):
    update_time = scrapy.Field()
    committee_name = scrapy.Field()

    conclusion = scrapy.Field()

    review_time = scrapy.Field()

    register_number = scrapy.Field()