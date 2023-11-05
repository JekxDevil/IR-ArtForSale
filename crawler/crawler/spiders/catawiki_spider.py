import scrapy

class CatawikiSpider(scrapy.Spider):

    name = "catawiki"

    start_urls = ["https://www.catawiki.com/en/",]

    def __init__(self, tags=None, artists=None, searches=None, **kwargs):
        self.default_tags = ["117-modern-contemporary-art", 
                             "746-photography", "1145-posters", "91-classical-art"]
        if tags == 'null':
            tags = []
        elif tags:
            tags = tags.split(',')
        else:
            tags = self.default_tags

        if searches:
            searches = searches.split(',')
            for query in searches:
                tags.append(query)

        # create an url for each tag
        self.start_urls = [
            f'https://www.catawiki.com/en/c/{tag}' for tag in tags]

        self.artists_urls = []
        if artists:
            self.artists_urls = artists.split(',')

        super().__init__(**kwargs)
    

    def parse(self, response):
        """ 
        Func called for every crawled page
        response param has website res
        """
        card = response.xpath("//a[@class='c-extended-lot-card__overlay']")
        link = response.xpath("//a[@class='c-extended-lot-card__overlay']/@href")
        for elem in card:
            author = elem.xpath("//h3[@class='c-extended-lot-card__title']/text()").get()
            type = elem.xpath("//p[@class='c-extended-lot-card__description u-color-mid-gray u-m-t-sm-xxs c-extended-lot-card__description__truncated']/text()").get()
            img = elem.xpath("//img[@data-testid='lot-card-extended-image']/@src").get()
            yield{"author": author, "type" : type, "img" : img, "link" : link}

        next_page = response.xpath('//a[@data-testid="next-page-link"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
 
