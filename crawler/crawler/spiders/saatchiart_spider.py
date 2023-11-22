from typing import Any
import scrapy


class SaatChiSpider(scrapy.Spider):
    name = "saatchi"
    start_urls = ["https://www.saatchiart.com", ]

    def __init__(self, tags=None, artists=None, searches=None, **kwargs):
        self.default_tags = ["abstract-expressionism", "contemporary", "contemporary-chinese-art", "contemporary-pop",
                             "constructivism", "cubism", "design", "impressionist-and-modern", "mixed-media",
                             "old-masters", "painting", "photography", "post-war", "prints", "sculpture",
                             "street-art", "surrealism", "works-on-paper", "young-british-artist", "pop-art"]

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

        # naive: create an url for each tag
        self.start_urls = [f'https://www.saatchiart.com/all?quert={tag}' for tag in tags]

        self.artists_urls = []
        if artists:
            self.artists_urls = artists.split(',')

        super().__init__(**kwargs)
    
    def parse(self, response):
        columns = response.xpath(
            "//div[@class='sc-16y3x88-1 fZtzVV']")
        for elem in columns:
            url = elem.xpath('//div[@data-type="artwork-image"]//a/@href').get()

            # href_item_page = elem.xpath('')
            if url:
                # Ensure that the URL is absolute
                url = response.urljoin(url)
                yield scrapy.Request(url, callback=self.parseArt)

        next_page = response.xpath('//a[@data-type="next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parseArt(self, response):
        price = response.xpath("//div[@class='krw7aj-0 uyv957-3 kpRguR bGUIw']/text()").get()
        value = response.xpath("//div[@class='krw7aj-0 uyv957-3 kpRguR bGUIw']//span/text()").get()
        price = price + " " + value
        author = response.xpath("//a[@data-type='profile']/text()").get()
        description = response.xpath('//p[@data-type="description"]/text()').get()
        title = response.xpath("//h1[@data-type='title-text']/text()").get()
        img = response.xpath('//div[@data-type="image"]//img/@src').get()
        keywords = response.css('div[data-type="keyword-row"] a::text').getall()
        creation_subject = response.xpath("//div[@data-type='about-artwork']"
                                          "//div[@data-type='accordion-content']"
                                          "//div//p//*[@data-type='accordion-sub-value']/text()").getall()
        materials_styles_medium = response.xpath("//div[@data-type='about-artwork']"
                                                 "//div[@data-type='accordion-content']"
                                                 "//div//p//*[@data-type='accordion-sub-value']//a/text()").getall()

        yield {
            'img': img,
            'author': author,
            'title': title,
            'price': price,
            'description': description,
            'url': response.url,
            'tags': keywords + creation_subject + materials_styles_medium
        }
