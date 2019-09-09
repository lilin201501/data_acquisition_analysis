# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



import json
import pymysql

class JSONPipeline(object):

    def __init__(self):
        self.file = open('book_info.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()

class DBPipeline(object):

    def __init__(self):
        print("执行这里！")
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            db='Scrapy',
            user='root',
            passwd='1234'
        )

        # 数据库游标，用于操作数据库
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # 将信息写入数据库
            self.cursor.execute("INSERT INTO qidian(title,author,information,introduction,word_num,clicks_num,recommended_num) VALUES (%s,%s,%s,%s,%s,%s,%s)",(item['title'],item['author'],item['information'],item['Introduction'],item['word_num'],item['clicks_num'],item['recommended_num']))
            # 提交信息
            self.connect.commit()
        except Exception as e:
            # 输出错误信息
            print(e)

        return item

    def close_spider(self, spider):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.connect.close()