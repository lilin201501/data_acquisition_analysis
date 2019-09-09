from scrapy.cmdline import execute

execute(["scrapy","crawl","stock","-o","item.json"])