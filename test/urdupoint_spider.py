import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import HtmlResponse
from scrapy.utils.project import get_project_settings
from scrapy import signals
from scrapy.signalmanager import dispatcher

class UrdupointSpider(scrapy.Spider):
    name = 'urdupoint'
    start_urls = ['https://www.urdupoint.com/']

    def __init__(self, *args, **kwargs):
        super(UrdupointSpider, self).__init__(*args, **kwargs)
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)

    def parse(self, response):
        # Extract the title
        title = response.xpath('//title/text()').get()
        print("Title:", title)

        # Extract the paragraphs
        paragraphs = response.xpath('//p/text()').getall()
        for paragraph in paragraphs:
            print("Paragraph:", paragraph)

    def spider_closed(self, spider):
        print("Spider closed: ", spider.name)

if __name__ == "__main__":
    settings = get_project_settings()
    settings.set('LOG_LEVEL', 'INFO')
    settings.set('FEEDS', {'output.json': {'format': 'json'}})

    process = CrawlerProcess(settings)
    process.crawl(UrdupointSpider)
    process.start()
