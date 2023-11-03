import scrapy

class Society6Spider(scrapy.Spider):

    name = "society6"

    start_urls = ["https://www.society6.com",]

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
            f'https://www.artsy.net/search?q={tag}&context={tag}sort=best_match' for tag in tags]

        self.artists_urls = []
        if artists:
            self.artists_urls = artists.split(',')

        super().__init__(**kwargs)

    def parse(self, response):
        """ 
        Func called for every crawled page
        response param has website res
        """
        column = response.xpath("//div[@class='cards_productCards_G7BsC undefined cardsGrid_productCards_2LjvG']")
        for elem in column:
            
            img = elem.xpath("//div[@class='imageWrapperInner_imagev2_2qEdJ']//img/@src").get()
            name = elem.xpath("//a[@class='title_productCard_2vL7c']/text()").get()
            author = elem.xpath("//a[@class='authorLink_productCard_1ix0F']/text()").get()
            price = elem.xpath("//div[@class='price_productCard_3OU93']//span/text()").get()
            tag = elem.xpath("//div[@class='productType_productCard_2Zmkv']/text()").get()
            if img:
                img = img.strip()
            if author:
                author = author.strip()
            if name:
                name = name.strip()
            if price:
                price = price.strip()
                
            href_item_page = elem.xpath('')
            if  author or name or price:
                yield {'img': img, 'author': author, 'name': name, 'price': price, 'category': tag,
                       'description': Society6Spider.get_description(href_item_page) }
        next_page = response.xpath("//a[@class='paginationArrow_paginationArrow_Qzhy6 paginationArrowNext_paginationArrow_SVStK']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        @staticmethod
        def get_description():
            pass
 
