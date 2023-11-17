# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import csv
from scrapy.exceptions import DropItem

class DongchediScraperPipeline(object):
    def open_spider(self, spider):
        # 在爬虫开始时打开文件
        self.file = open('dongchedi_data.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['序号', '品牌ID', '品牌名称', '封面图URL', '车型名称', '官方指导价', '款式数量', '评分'])

    def close_spider(self, spider):
        # 在爬虫结束时关闭文件
        self.file.close()

    def process_item(self, item, spider):
        # 处理每个项目，写入CSV文件
        if self.is_item_valid(item):
            self.writer.writerow([
                item.get('serial_number', ''),
                item.get('brand_id', ''),
                item.get('brand_name', ''),
                item.get('cover_url', ''),
                item.get('outter_name', ''),
                item.get('official_price', ''),
                item.get('count', ''),
                item.get('dcar_score', '')
            ])
            return item
        else:
            raise DropItem(f"Missing fields in {item}")

    def is_item_valid(self, item):
        # 验证项目是否包含所有必要字段
        required_fields = ['serial_number', 'brand_id', 'brand_name', 'cover_url', 'outter_name', 'official_price', 'count', 'dcar_score']
        return all(field in item for field in required_fields)
