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
            url = elem.xpath("//a[@class='RouterLink__RouterAwareLink-sc-1nwbtp5-0 hbVDGn GridItem__Link-d2n1vy-0 JunK']/@href").get()

                
            # href_item_page = elem.xpath('')
            if url:
            # Ensure that the URL is absolute
                url = response.urljoin(url)

                yield scrapy.Request(url, callback=lambda response, tag=tag: self.parseArt(response, tag))


        next_page = response.xpath('//a[@data-testid="next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


    def parseArt(self, response, tag):
        price = response.xpath("//div[@class='Box-sc-15se88d-0 Text-sc-18gcpao-0 eXbAnU drBoOI']/text()").get()
        author = response.xpath("//a[@class='RouterLink__RouterAwareLink-sc-1nwbtp5-0 dikvRF ArtworkSidebarArtists__StyledArtistLink-eqhzb8-0 jdgrPD']/text()").get()
        title = response.xpath("//h1[@class='Box-sc-15se88d-0 Text-sc-18gcpao-0 caIGcn bhlKfb']//i/text()").get()
        img = response.xpath('//img[@data-testid="artwork-lightbox-image"]/@src').get()

        yield {'img': img, 
               'author': author,
               'title': title, 
               'price': price ,
               'url' : response.url}

    @staticmethod
    def get_description():
        pass