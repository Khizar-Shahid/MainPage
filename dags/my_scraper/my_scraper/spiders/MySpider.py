import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        # Extracting the content using CSS selectors
        books = response.css('article.product_pod')
        
        for book in books:
            title = book.css('h3 a::attr(title)').get()
            price = book.css('div.product_price p.price_color::text').get()
            
            yield {
                'title': title,
                'price': price,
            }






