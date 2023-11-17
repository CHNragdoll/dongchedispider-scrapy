# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DongchediItem(scrapy.Item):
    # 定义爬虫中使用的字段
    serial_number = scrapy.Field()  # 序号
    brand_id = scrapy.Field()  # 品牌ID
    brand_name = scrapy.Field()  # 品牌名称
    cover_url = scrapy.Field()  # 封面图URL
    outter_name = scrapy.Field()  # 车型名称
    official_price = scrapy.Field()  # 官方指导价
    count = scrapy.Field()  # 款式数量
    dcar_score = scrapy.Field()  # 评分
