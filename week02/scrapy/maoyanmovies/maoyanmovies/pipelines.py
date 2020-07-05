# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from maoyanmovies.store import StoreInfo


class MaoyanmoviesPipeline:
    def process_item(self, item, spider):
        title = item['title']
        genre = item['genre']
        release_time = item['release_time']

        # output = str(item['title']) + ',' + str(item['genre']) + ',' + str(item['release_time']) + '\n'
        # with open('./movie.csv', 'a+', encoding='UTF-8') as file:
        #     file.write(output)
        # return item
        print(title, genre, release_time)
        print(1212121212121212121212)
        sqls = 'insert into films (`name`, `genre`, `release_time`) values("' + title + '","' + genre + '","' + release_time + '");'
        store = StoreInfo()
        store.store(sqls)
