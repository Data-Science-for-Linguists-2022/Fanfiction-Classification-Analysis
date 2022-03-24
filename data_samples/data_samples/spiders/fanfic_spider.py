import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FanficSpider(CrawlSpider):
    name = 'fanfic-1'
    allowed_domains = ['archiveofourown.org']
    start_urls = ['https://archiveofourown.org/media']

    SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'
    CONCURRENT_REQUESTS = 5000
    REACTOR_THREADPOOL_MAXSIZE = 1000
    RETRY_ENABLED = False
    DOWNLOAD_TIMEOUT = 15
    LOG_LEVEL = 'INFO'
    COOKIES_ENABLED = False
    DEPTH_PRIORITY = 1
    SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
    SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

    rules = (
        Rule(LinkExtractor(allow=('tags'), deny=('users', ))),
        Rule(LinkExtractor(allow=('works', )), callback='parse'),
    )

    def parse(self, response):
        page = response.url.split("/")[-3]
        nums = re.search('[0-9]+', page)
        if(nums):
            filename = f'{page}.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log(f'Saved file {filename}')
            for href in response.xpath('//a/@href').getall():
                yield scrapy.Request(response.urljoin(href), self.parse)
