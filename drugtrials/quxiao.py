# item['register_number'],
# # 适应症
# item['adaptation_disease'],
# # 通俗题目
# item['Pilot_topic'],
# # 正式题目
# item['major_topic'],
# # 实验方案编号
# item['project_number'],
# # 临床申请受理号
# item['Clinical_application'],
# # 药物名称
# item['drug_name'],
# # 药物类型
# item['drug_type'],
# # 申办者名称
# item['applicant_name'],
# # 联系人姓名
# item['contact_name'],
# # 联系人电话
# item['contact_phone'],
# # 联系人邮政地址
# item['contact_address'],
# # 试验项目经费来源
# item['project_fund'],
# # 联系人邮箱
# item['contact_email'],
# # 联系人邮编
# item['contact_code'],
#
# # 试验目的
# item['study_goal'],
# # 试验设计
# item['study_class'],
# # 实验分期
# item['study_fenqi'],
# # 实验类型
# item['study_type'],
# # 随机化
# item['study_random'],
# # 盲法
# item['study_blinding'],
# # 测试范围
# item['study_range'],
# # 受试者年龄
# item['accept_test_age'],
# # 受试者性别
# item['accept_test_sex'],
# # 健康受试者
# item['health_test_person'],
# # 入选标准
# item['inclusion_criteria'],
# # 排除标准
# item['exclusion_criteria'],
# # 目标入组人数
# item['except_person_number'],
# # 实际入组人数
# item['actual_person_number'],
# # 数据安全监察委员会
# item['data_safety_regulatory'],
# # 为受试者购买试验伤害保险
# item['for_test_buy_insurance'],
# # 第一例受试者入组日期
# item['first_test_person_time'],
# # 试验终止日期
# item['test_finish_time'],
#
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
#
# item['study_status'],
#
#
#
# item['drug_type'],
#
# item['drug_name'] ,
#
# item['drug_directions'] ,
#
# item['register_number'] ,
#
#
#
#
#
#
#
# item['indicators_type]  ,
#
# item['indicators_name]  ,
#
# item['indicators_time]  ,
#
# item['indicators_collect]  ,
#
# item['register_number]  ,
#
#
# item['research_name'] ,
#
# item['research_unit'] ,
#
# item['research_country'] ,
#
# ritem['esearch_province'] ,
#
# item['research_city'] ,
#
# item['register_number'] ,
#
#
# item['committee_name'] ,
#
# item['conclusion'] ,
#
# item['review_time'] ,
#
# item['register_number'] ,

sql = "insert into annual_meeting(xuezu,date,meeting_name,url,master,time,process_time,type,title,speaker,speaker_unit,remark) values(item['xuezu'],item['date'],item['meeting_name'],item['url'],item['master'],item['time'],item['process_time'],item['type'],item['title'],item['speaker'],item['speaker_unit'],item['remark'])"