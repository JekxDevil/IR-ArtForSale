import scrapy

class ArtsySpider(scrapy.Spider):

    name = "artsy"

    start_urls = ["https://www.artsy.net",]

    def parse(self, response):
        """ 
        Func called for every crawled page
        response param has website res
        """
        for elem in response.xpath("selector/*"):
            # scrap interested tags from site
            # yield scrapped dict
            pass

        next_page = response.xpath("selector/href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
 
