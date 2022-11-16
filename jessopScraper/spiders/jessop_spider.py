import scrapy
from ..items import JessopscraperItem

class jessop_spider(scrapy.Spider):
    name = 'jessop'
    start_urls = ['https://www.jessops.com/accessories/batteries-and-chargers?Main-Nav']

    def parse(self, response):
        items = JessopscraperItem()

        products = response.css('div.f-grid.prod-row')
        for product in products:
            title = product.css('div.details').css('a::text').extract_first()
            brand = product.css('div.details').css('img.product-brand::attr(alt)').extract_first()
            link =  product.css('div.details').css('a::attr(href)').get()
            link = 'https://www.jessops.com' + link
            image = product.css('img.f-width-1-1::attr(src)').get()
            price = product.css('p.price.larger::text').extract_first()
            about = product.css('ul.f-list.j-list').css('li::text').extract()

            items['title'] = title
            items['brand'] = brand
            items['link'] = link
            items['image'] = image
            items['price'] = price
            items['about'] = about

            yield items

        next_page = response.css('.f-active~ li+ li a::attr(href)').get()
        
        if next_page:
            yield response.follow(next_page, callback = self.parse)              
