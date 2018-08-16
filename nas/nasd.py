# -*- coding: utf-8 -*-
import scrapy
from nas.items import NasItem
from scrapy.http import Request

class NasSpider(scrapy.Spider):
    name = 'ipo'
    allowed_domains = ['www.nasdaq.com']
    start_urls = ['https://www.nasdaq.com/markets/ipos/activity.aspx?tab=pricings&month=2018-08']

    def parse(self, response):
        item = NasItem()
        for box in response.xpath('//div[@id="tabpane1"]/div[@class="genTable"]/table/tbody/tr'):
            item['name'] = box.xpath('./td/a/text()').extract_first()
            item['symbol'] = box.xpath('./td[2]/a/text()').extract_first()
            item['mkt'] = box.xpath('./td[3]/text()').extract()
            item['price'] = box.xpath('./td[4]/text()').extract_first()
            item['shares']= box.xpath('./td[5]/text()').extract_first()
            item['offer'] = box.xpath('./td[6]/text()').extract_first()
            item['date'] = box.xpath('./td[7]/text()').extract_first()
            if len(item['mkt']) == 0:
                item['mkt'] = box.xpath('./td[3]/a/text()').extract()
            else:
                pass
            yield item

        next_page = response.xpath('//div[@class="ipo-pagination-div"]/a[@id="two_column_main_content_hlprev1"]/@href').extract()
        if next_page:
            next_page = next_page[0]
            next_page_url = response.urljoin(next_page)
            yield Request(next_page_url, callback=self.parse, dont_filter=False)
        else:
            print(str(next_page))

