### 目标：
爬取懂车帝目标地区的所有汽油车的 '品牌ID', '品牌名称', '封面图URL', '车型名称', '官方指导价', '款式数量', '评分'并把输出的数据加上序号

### 1. 安装Scrapy框架：

确保您已经安装了Python和pip。如果您在安装Scrapy时遇到了连接超时的问题，可能是由于网络连接问题、代理设置或者PyPI服务器不可用造成的。

- 检查您的网络连接。
- 如果您在中国大陆，可能需要使用镜像源，如使用以下命令通过清华大学开源软件镜像站（TUNA）来安装Scrapy：

```bash
pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple
```

如果没有上述问题，您可以直接安装Scrapy：

```bash
pip install scrapy
```

### 2. 使用Scrapy命令创建项目和爬虫文件：

在您选择的目录中创建一个新的Scrapy项目：

```bash
scrapy startproject dongchedi_scraper
```

在项目内创建一个名为 `dongchedi` 的爬虫，目标网站设置为 `www.dongchedi.com`：

```bash
cd dongchedi_scraper
scrapy genspider dongchedi www.dongchedi.com
```

### 3. 编写爬虫代码：

找到 `dongchedi.py` 文件，在 `dongchedi_scraper/spiders` 目录下编辑。这包括定义爬虫的名称、允许的域名、起始URL等。
*目标图
![IMG_1434](https://github.com/CHNragdoll/dongchedispider-scrapy/assets/114509813/375b800f-9928-43db-8e5d-c99be191f4f4)


### 4. 定义 Item

在 `items.py` 文件中定义您的 Item 类。这是用于存储爬取数据的结构。

### 5. 编写 Item Pipeline

在 `pipelines.py` 文件中编写管道（Pipeline）以处理爬虫返回的数据项（例如，保存到数据库或文件中）。

### 6. 配置项目设置

在 `settings.py` 文件中，配置项目的设置，如并发请求的数量、下载延迟、管道启用等。

### 7. 运行爬虫：

您可以使用以下命令在项目目录下运行您的爬虫：

```bash
scrapy crawl dongchedi
```

