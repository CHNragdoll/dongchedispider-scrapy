import scrapy
from dongchedi_scraper.items import DongchediItem
import json
import math

class DongchediSpider(scrapy.Spider):
    name = 'dongchedi'  # 爬虫的名字，唯一标识一个爬虫
    allowed_domains = ['www.dongchedi.com']  # 限制爬虫爬取的域名范围
    start_url = 'https://www.dongchedi.com/motor/pc/car/brand/select_series_v2?aid=1839&app_name=auto_web_pc'  # 爬虫开始爬取的 URL

    max_pages = 45  # 设置爬虫最大爬取的页数
    item_count = 0  # 用于记录爬取的项目数量，为每个项目编号

    def start_requests(self):
        # 爬虫启动时的方法，向 start_url 发送请求
        yield scrapy.FormRequest(
            self.start_url,  # 请求的 URL
            formdata=self.get_form_data(1),  # 发送的表单数据
            callback=self.parse,  # 请求成功后的回调方法
            meta={'current_page': 1}  # 附加信息，当前页码为 1
        )

    def parse(self, response):
        # 解析响应内容的方法
        try:
            data = json.loads(response.text)  # 尝试将响应内容解析为 JSON
            if 'status' in data and data['status'] == 0:  # 检查 JSON 中的状态字段
                for item in data['data']['series']:  # 遍历 JSON 中的数据
                    self.item_count += 1  # 为每个项目增加编号
                    yield self.parse_item(item)  # 调用 parse_item 方法处理每个项目

                yield from self.handle_pagination(response, data)  # 处理分页
            else:
                self.logger.error(f'No data found or error in response: {response.url}')
        except json.JSONDecodeError as e:
            self.logger.error(f'Error parsing JSON: {e}, URL: {response.url}')

    def handle_pagination(self, response, data):
        # 处理分页的方法
        total_count = data['data']['series_count']  # 总数据量
        total_page = math.ceil(total_count / 30)  # 计算总页数
        current_page = response.meta['current_page']  # 获取当前页码

        # 判断是否需要继续爬取下一页
        if current_page < total_page and current_page < self.max_pages:
            next_page = current_page + 1  # 准备爬取的下一页页码
            yield scrapy.FormRequest(
                self.start_url,
                formdata=self.get_form_data(next_page),  # 获取下一页的表单数据
                callback=self.parse,  # 设置回调函数为 parse 方法
                meta={'current_page': next_page}  # 更新当前页码
            )

    def get_form_data(self, page):
        # 根据页码生成请求的表单数据
        return {
            "fuel_form": "1",  # 燃料类型参数
            "sort_new": "hot_desc",  # 排序参数
            "city_name": "石家庄",  # 城市参数
            "limit": "30",  # 每页显示的条目数
            "page": str(page)  # 当前页码
        }

    def parse_item(self, item):
        # 解析并处理每个项目的数据
        return DongchediItem(
            serial_number=self.item_count,  # 项目序号
            brand_id=item['brand_id'],  # 品牌ID
            brand_name=item['brand_name'],  # 品牌名称
            cover_url=item['cover_url'],  # 封面图的 URL
            outter_name=item['outter_name'],  # 车型名称
            official_price=item['official_price'],  # 官方指导价
            count=item['count'],  # 款式数量
            dcar_score=item['dcar_score']  # 评分
        )
