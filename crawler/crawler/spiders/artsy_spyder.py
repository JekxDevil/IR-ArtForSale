from typing import Any
import scrapy


class ArtsySpider(scrapy.Spider):

    name = "artsy"

    start_urls = ["https://www.artsy.net", ]

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
            f'https://www.artsy.net/collection/{tag}' for tag in tags]

        self.artists_urls = []
        if artists:
            self.artists_urls = artists.split(',')

        super().__init__(**kwargs)
    
    def parse(self, response):
        columns = response.xpath(
            "//div[@class='Box-sc-15se88d-0 Flex-cw39ct-0 ArtworkGrid__InnerContainer-uextjn-1 LbPWX jdYVcL fresnel-greaterThanOrEqual-lg']")
        tag = response.xpath("//h1[@class='Box-sc-15se88d-0 Text-sc-18gcpao-0 eGPiVT bTXFzS']/text()").get()
        for elem in columns:
            img = elem.xpath('//div[@data-test="artworkGridItem"]//img/@src').get()

            author = elem.xpath(
                ".//div[@class='Box-sc-15se88d-0 Text-sc-18gcpao-0  ilQWRL']//span/text()").get()
            name = elem.xpath(
                ".//div[@class='Box-sc-15se88d-0 Text-sc-18gcpao-0 caIGcn iVSzqj']//i/text()").get()
            price = elem.xpath(
                ".//div[@class='Box-sc-15se88d-0 Text-sc-18gcpao-0 eXbAnU bfCidL']/text()").get()
            date = elem.xpath(".//div[@class='Box-sc-15se88d-0 Text-sc-18gcpao-0 caIGcn iVSzqj']/text()").get()

            if img:
                img = img.strip()
            if author:
                author = author.strip()
            if name:
                name = name.strip()
            if date:
                date = date.strip()
            if price:
                price = price.strip()
                
            # href_item_page = elem.xpath('')
            if  author or name or date or price:
                yield {'img': img, 'author': author, 'name': name, 'date':date, 'price': price, 'category': tag,
                       }

        next_page = response.xpath('//a[@data-testid="next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


    @staticmethod
    def get_description():
        pass