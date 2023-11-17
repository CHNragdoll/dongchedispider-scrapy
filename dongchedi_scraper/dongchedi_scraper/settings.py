# Scrapy settings for dongchedi_scraper project
# 为dongchedi_scraper项目定义Scrapy设置

# 此文件仅包含被认为重要或常用的设置项。您可以通过查阅文档了解更多设置：
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "dongchedi_scraper"  # 定义爬虫项目的名称

SPIDER_MODULES = ["dongchedi_scraper.spiders"]  # 指定爬虫模块的位置
NEWSPIDER_MODULE = "dongchedi_scraper.spiders"  # 指定新爬虫的模块

# 通过用户代理（User-Agent）来负责地进行爬取
DEFAULT_REQUEST_HEADERS = {  # 设置默认的请求头
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Referer': 'https://www.dongchedi.com/auto/library/x-x-x-x-x-x-1-x-x-x-x-x-x-x-x-x-x-x',
    'Origin': 'https://www.dongchedi.com',
}

ROBOTSTXT_OBEY = False  # 设置是否遵守robots.txt规则
DOWNLOAD_DELAY = 2  # 设置下载延迟为2秒，避免对服务器造成过大压力
CONCURRENT_REQUESTS = 16  # 设置同时发送的最大并发请求为16
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
COOKIES_ENABLED = False  # 禁用Cookies
LOG_LEVEL = 'INFO'  # 设置日志级别为INFO
AUTOTHROTTLE_ENABLED = True  # 启用自动限速
AUTOTHROTTLE_START_DELAY = 5  # 自动限速的起始延迟时间
AUTOTHROTTLE_MAX_DELAY = 60  # 自动限速的最大延迟时间
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # 目标并发数
AUTOTHROTTLE_DEBUG = False  # 关闭自动限速的调试模式

# 重写默认请求头
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
}

# 启用或禁用爬虫中间件
SPIDER_MIDDLEWARES = {
    "dongchedi_scraper.middlewares.DongchediScraperSpiderMiddleware": 543,
}

# 启用或禁用下载器中间件
DOWNLOADER_MIDDLEWARES = {
    "dongchedi_scraper.middlewares.DongchediScraperDownloaderMiddleware": 543,
}

# 启用或禁用扩展
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# 配置项目管道
ITEM_PIPELINES = {
    "dongchedi_scraper.pipelines.DongchediScraperPipeline": 300,  # 指定DongchediScraperPipeline的优先级
}

# 设置HTTP缓存的相关配置（默认禁用）
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# 设置默认值即将过时的设置项，确保向前兼容
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"  # 设置导出文件的编码为utf-8
