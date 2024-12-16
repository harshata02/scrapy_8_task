import scrapy


class BookInfoSpider(scrapy.Spider):
    name = "book_info"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        book_titles=response.css('a[href]::attr(title)').getall()
        for titles in book_titles:
            yield{
                'titles':titles
            }
    
            
        

        
    



            
        
        
