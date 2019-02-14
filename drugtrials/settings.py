# -*- coding: utf-8 -*-

BOT_NAME = 'drugtrials'

SPIDER_MODULES = ['drugtrials.spiders']
NEWSPIDER_MODULE = 'drugtrials.spiders'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 16

LOG_LEVEL = 'INFO'
#DOWNLOAD_DELAY = 3

#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16


COOKIES_ENABLED = False



#SPIDER_MIDDLEWARES = {
#    'drugtrials.middlewares.DrugtrialsSpiderMiddleware': 543,
#}


DOWNLOADER_MIDDLEWARES = {
   'drugtrials.middlewares.RandomProxyMiddleware': 543,
}



ITEM_PIPELINES = {
   # 'drugtrials.pipelines.DrugtrialsPipeline': 300,
'drugtrials.pipelines.mysqlpipeline':400,

}
mongo_host = 'localhost'
mongo_port = 27017