import scrapy

class CrawlingSpider(scrapy.Spider):
    name = 'crawling'
    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/super-gene-optimization-fluid/chapter-501-a-hero-who-cares/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    limit = 9

    def parse(self, response):

        for next_page in response.css('a.prevchap'):
            if self.limit > 0 :
             yield response.follow(next_page, self.parse)
             self.limit -= 1

        for title in response.css('.post-title.mb-4.font-weight-bold'):
            yield {'title': title.css('::text').get()}

        for link in response.css('div.chapter-fill'):
            yield {'isi': link.css('p::text').getall()}

        for link in response.css('a.prevchap'):
            yield {'link': link.css('::attr(href)').get()}