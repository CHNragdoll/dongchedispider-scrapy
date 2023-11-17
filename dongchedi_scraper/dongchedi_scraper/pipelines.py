# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 定义你的项目管道
# 别忘了将你的管道添加到 ITEM_PIPELINES 设置中
# 参考文档：https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter  # 从itemadapter导入ItemAdapter，用于不同项目类型的单一接口处理

import csv  # 导入csv模块，用于操作CSV文件
from scrapy.exceptions import DropItem  # 从scrapy.exceptions导入DropItem，用于在项目不符合要求时抛出异常

class DongchediScraperPipeline(object):  # 定义一个管道类
    def open_spider(self, spider):
        # 爬虫开始时执行的方法
        self.file = open('dongchedi_data.csv', 'w', newline='', encoding='utf-8')  # 打开一个CSV文件用于写入数据
        self.writer = csv.writer(self.file)  # 创建一个CSV文件写入器
        self.writer.writerow(['序号', '品牌ID', '品牌名称', '封面图URL', '车型名称', '官方指导价', '款式数量', '评分'])  # 写入表头

    def close_spider(self, spider):
        # 爬虫结束时执行的方法
        self.file.close()  # 关闭文件

    def process_item(self, item, spider):
        # 处理每一个从爬虫传来的项目
        if self.is_item_valid(item):  # 如果项目有效
            self.writer.writerow([  # 将项目数据写入CSV文件
                item.get('serial_number', ''),  # 获取项目的序号
                item.get('brand_id', ''),  # 获取品牌ID
                item.get('brand_name', ''),  # 获取品牌名称
                item.get('cover_url', ''),  # 获取封面图URL
                item.get('outter_name', ''),  # 获取车型名称
                item.get('official_price', ''),  # 获取官方指导价
                item.get('count', ''),  # 获取款式数量
                item.get('dcar_score', '')  # 获取评分
            ])
            return item  # 返回处理后的项目
        else:
            raise DropItem(f"Missing fields in {item}")  # 如果项目不完整，抛出异常

    def is_item_valid(self, item):
        # 检查项目是否有效的方法
        required_fields = ['serial_number', 'brand_id', 'brand_name', 'cover_url', 'outter_name', 'official_price', 'count', 'dcar_score']  # 定义必须的字段列表
        return all(field in item for field in required_fields)  # 检查项目是否包含所有必须字段
