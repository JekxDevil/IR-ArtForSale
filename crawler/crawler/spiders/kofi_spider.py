import scrapy

class KofiSpider(scrapy.Spider):

    name = "kofi"

    start_urls = ["https://www.ko-fi.com",]

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
 
