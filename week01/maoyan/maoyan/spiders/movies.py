import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def start_requests(self):
    #     return scrapy.Request(url=self.start_urls[0], callback=self.parse)

    # 解析
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        movie_list = []
        for movie in movies[:10]:
            item = MaoyanItem()
            movie_infos = movie.xpath('.//div[contains(@class,"movie-hover-title")]')
            item['title'] = movie_infos[0].xpath('./@title').extract_first()
            item['genre'] = movie_infos[1].xpath('./text()').extract()[1].strip()
            item['release_time'] = movie_infos[3].xpath('./text()').extract()[1].strip()
            movie_list.append(item)

        return movie_list
