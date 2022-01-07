# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class HolidaysPipeline:

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = '12345' # your password
        database = 'db'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into scrapy(Day,Date,Holiday_name,Type,comments) values(%s,%s,%s,%s,%s)",
                         (item['Day'],item['Date'],item['Holiday_name'],item['Type'],item['comments']))
        self.connection.commit()
        return item
