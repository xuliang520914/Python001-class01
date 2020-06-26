# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter

class MaoyanPipeline:
    def process_item(self, item, spider):
        output = str(item['title']) + ',' + str(item['genre']) + ',' + str(item['release_time']) + '\n'
        with open('./movie.csv', 'a+', encoding='UTF-8') as file:
            file.write(output)
        return item
