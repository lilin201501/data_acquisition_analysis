# 1创建Scrapy爬虫项目
* Scrapy startproject stockstar
* 查看settings.py,确定ROBOTSTXT_OBEY选项设置

# 2定义一个item容器
首先需要对所要爬取的网页数据进行分析，定义所爬去记录的数据结构。

# 3定义setting文件进行爬虫基本设置

# 4编写爬虫逻辑
cd stockstar
scrapy genspider stock quote.stockstar.com

# 5代码调试
