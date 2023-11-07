from typing import Any
import scrapy


class ArtFinderSpider(scrapy.Spider):

    name = "artfinder"

    start_urls = ["https://www.artfinder.com", ]

    def __init__(self, tags=None, artists=None, searches=None, **kwargs):
        self.default_tags = ["abstract-expressionism", "contemporary",
                             "contemporary-chinese-art", "contemporary-pop",
                             "constructivism", "cubism", "design",
                             "impressionist-and-modern", "mixed-media",
                             "old-masters", "painting", "photography",
                             "post-war", "prints", "sculpture", "street-art",
                             "surrealism", "works-on-paper", "young-british-artist", "pop-art"]
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
            f'https://www.artfinder.com/art/sort-best_match/paginate-60/q-{tag}/availability-true/' for tag in tags]

        self.artists_urls = []
        if artists:
            self.artists_urls = artists.split(',')

        super().__init__(**kwargs)
    
    def parse(self, response):
        columns = response.xpath(
        "//section[@class='sc-373cc321-0 eZjxMK']")
        for elem in columns:
            img = elem.xpath('//div[@class="sc-f5f2eb2f-0 kJBexs"]//figure//img/@src').get()
            url = elem.xpath('//div[@class="sc-f5f2eb2f-0 kJBexs"]//a/@href').get()
            author = elem.xpath(
            ".//div[@class='sc-f5f2eb2f-0 kJBexs']//section//h5/text()").get()
            type = elem.xpath(
            ".//div[@class='sc-f5f2eb2f-0 kJBexs']//section//h6/text()").get()

            if img:
                img = img.strip()
            if author:
                author = author.strip()

            if url:
            # Ensure that the URL is absolute
                url = response.urljoin(url)

                yield scrapy.Request(url, callback=self.parseArt, meta={'img': img, 'author': author, 'type': type})

        next_page = response.xpath('//a[@class="sc-382f794-0 huZRiQ"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parseArt(self, response):
        price = response.xpath("//span[@class='header-art']/text()").get()
        author = response.xpath("//h6[@class='body1']//a[2]/text()").get()
        description = response.xpath('//p[@class="body1"]/text()').get()
        title = response.xpath("//div[@class='tab-pane active']//h5/text()").get()
        img = response.xpath('//div[@class="carousel-figure-center"]//figure//img/@src').get()
        all_tags = response.xpath('//div[@class="artwork-description"]//a/text()').getall()
        tags = " ".join(all_tags).strip()

        yield {'img': img, 
               'author': author,
               'title': title, 
               'price': price ,
               'description': description,
               'tags': tags}

    @staticmethod
    def get_description():
        pass
