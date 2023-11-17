import scrapy  # 引入scrapy框架
from dongchedi_scraper.items import DongchediItem  # 从项目中引入自定义的Item类
import json  # 导入json模块，用于解析JSON格式的数据
import math  # 导入math模块，提供数学运算函数

class DongchediSpider(scrapy.Spider):  # 定义一个继承自scrapy.Spider的爬虫类
    name = 'dongchedi'  # 设置爬虫的名称
    allowed_domains = ['www.dongchedi.com']  # 限制爬虫只能爬取指定域名下的数据
    start_url = 'https://www.dongchedi.com/motor/pc/car/brand/select_series_v2?aid=1839&app_name=auto_web_pc'  # 爬虫开始爬取的URL地址
    max_pages = 45  # 设置爬虫爬取的最大页数
    item_count = 0  # 设置一个计数器，用于统计已爬取的项目数量

    def start_requests(self):  # 定义一个方法，用于发送初始请求
        yield scrapy.FormRequest(
            self.start_url,  # 指定请求的URL
            formdata=self.get_form_data(1),  # 设置请求的表单数据
            callback=self.parse,  # 指定响应的处理函数
            meta={'current_page': 1}  # 携带额外信息：当前页码
        )

    def parse(self, response):  # 定义处理响应的方法
        try:
            data = json.loads(response.text)  # 解析响应数据为JSON格式
            if 'status' in data and data['status'] == 0:  # 检查响应数据中的状态
                for item in data['data']['series']:  # 遍历JSON中的数据项
                    self.item_count += 1  # 项目计数器加1
                    yield self.parse_item(item)  # 对每个项目调用解析方法
                yield from self.handle_pagination(response, data)  # 处理分页
        except json.JSONDecodeError as e:
            self.logger.error(f'Error parsing JSON: {e}, URL: {response.url}')  # 记录JSON解析错误

    def handle_pagination(self, response, data):  # 定义处理分页的方法
        total_count = data['data']['series_count']  # 获取数据总数
        total_page = math.ceil(total_count / 30)  # 计算总页数
        current_page = response.meta['current_page']  # 获取当前页码

        if current_page < total_page and current_page < self.max_pages:  # 检查是否需要爬取下一页
            next_page = current_page + 1  # 下一页的页码
            yield scrapy.FormRequest(
                self.start_url,
                formdata=self.get_form_data(next_page),  # 获取下一页的表单数据
                callback=self.parse,  # 指定回调函数为当前解析方法
                meta={'current_page': next_page}  # 更新页码信息
            )

    def get_form_data(self, page):  # 定义生成表单数据的方法
        return {
            "fuel_form": "1",  # 燃料类型
            "sort_new": "hot_desc",  # 排序方式
            "city_name": "石家庄",  # 城市名称
            "limit": "30",  # 每页数据限制
            "page": str(page)  # 当前页码
        }

    def parse_item(self, item):  # 定义解析单个项目的方法
        return DongchediItem(
            serial_number=self.item_count,  # 项目序号
            brand_id=item['brand_id'],  # 品牌ID
            brand_name=item['brand_name'],  # 品牌名称
            cover_url=item['cover_url'],  # 封面图URL
            outter_name=item['outter_name'],  # 车型名称
            official_price=item['official_price'],  # 官方价格
            count=item['count'],  # 车型数量
            dcar_score=item['dcar_score']  # 车型评分
        )
