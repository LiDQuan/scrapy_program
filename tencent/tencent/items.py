# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名
    name = scrapy.Field()
	# 链接详情
    link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 人数
    position_people = scrapy.Field()
    # 地点
    position_site = scrapy.Field()
    # 发布时间
    position_time = scrapy.Field()
