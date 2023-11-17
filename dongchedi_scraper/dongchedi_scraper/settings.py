
# Scrapy settings for dongchedi_scraper project
# 为dongchedi_scraper项目定义Scrapy设置
#
# 由于简洁性，此文件仅包含被认为重要或常用的设置项。您可以通过查阅文档了解更多设置：
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "dongchedi_scraper"  # 定义爬虫项目的名称

SPIDER_MODULES = ["dongchedi_scraper.spiders"]  # 指定爬虫模块的位置
NEWSPIDER_MODULE = "dongchedi_scraper.spiders"  # 指定新爬虫的模块

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 通过用户代理（User-Agent）来负责地进行爬取
DEFAULT_REQUEST_HEADERS = {  # 设置默认的请求头
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Referer': 'https://www.dongchedi.com/auto/library/x-x-x-x-x-x-1-x-x-x-x-x-x-x-x-x-x-x',
    'Origin': 'https://www.dongchedi.com',
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 设置是否遵守robots.txt规则
DOWNLOAD_DELAY = 2  # 设置下载延迟为2秒
CONCURRENT_REQUESTS = 16  # 设置同时发送的最大并发请求为16

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 配置Scrapy执行的最大并发请求数（默认为16）
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# 为同一网站的请求配置延迟（默认为0）
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# 参考 https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 参考自动限速设置和文档
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 下载延迟设置将只遵循以下之一：
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 禁用Cookies（默认启用）
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 禁用Telnet控制台（默认启用）
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 重写默认的请求头
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
}

# Enable or disable spider middlewares
# 启用或禁用爬虫中间件
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# 参见 https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   "dongchedi_scraper.middlewares.DongchediScraperSpiderMiddleware": 543,
}

# Enable or disable downloader middlewares
# 启用或禁用下载器中间件
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 参见 https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "dongchedi_scraper.middlewares.DongchediScraperDownloaderMiddleware": 543,
}

# Enable or disable extensions
# 启用或禁用扩展
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# 参见 https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# 配置项目管道
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 参见 https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "dongchedi_scraper.pipelines.DongchediScraperPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# 启用并配置自动限速扩展（默认禁用）
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# 参见 https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 在高延迟情况下设置的最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# Scrapy应该并行发送到每个远程服务器的平均请求数
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 启用显示每个接收到的响应的限速统计信息：
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# 启用并配置HTTP缓存（默认禁用）
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 参见 https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
# 将默认值已过时的设置项设置为未来兼容的值
REQUEST_FINGERPRINTER_IMPLEMENTATION = “2.7”
TWISTED_REACTOR = “twisted.internet.asyncioreactor.AsyncioSelectorReactor”
FEED_EXPORT_ENCODING = “utf-8”  # 设置输出数据编码为utf-8
