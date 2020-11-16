# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyspiderPipeline:
    def process_item(self, item, spider):
        with open('result.txt', 'a+', encoding='utf-8-sig') as f:
            mystr = item['content']+"\n"
            f.write(mystr)
        return item
