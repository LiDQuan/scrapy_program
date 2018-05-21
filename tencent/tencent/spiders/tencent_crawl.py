# -*- coding: utf-8 -*-
import scrapy
import sys
# 这里显示红波浪线，但是scrapy运行起来却又没问题，这个不知道算不算是
from tencent.items import TencentItem
sys.stderr = sys.stdout


class TencentCrawlSpider(scrapy.Spider):
    name = 'tencent_crawl'
    allowed_domains = ['tencent.com']
    # 该函数表示scrapy框架从哪个url开始，当二次开始需要传递url时，则无需该变量
    url = "https://hr.tencent.com/position.php?keywords=&lid=0&tid=87&start="
    page = 0
    start_urls = [
        url + str(page)
    ]

    # 默认处理爬虫数据函数，最后要yield回调数据
    def parse(self, response):
        for eath in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 将各自的变量存放进来
            # 创建变量
            temp = TencentItem()
            # 职位名称
            temp['name'] = eath.xpath("./td[1]/a/text()").extract()[0]
            # 链接详情
            temp['link'] = eath.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            temp['position_type'] = eath.xpath("./td[2]/text()").extract()[0]
            # 人数
            temp['position_people'] = eath.xpath("./td[3]/text()").extract()[0]
            # 地点
            temp['position_site'] = eath.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            temp['position_time'] = eath.xpath("./td[5]/text()").extract()[0]
            # 将数据传入管道文件，进行存储
            yield temp
        # 设置爬虫翻页，当爬虫页数小于100时，page自动加10，
        if self.page < 100:
            self.page =+ 10
        # 每处理完一次数据后，重新发送下一页页面请求
        # 拼接url后，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.page), callback=self.parse)