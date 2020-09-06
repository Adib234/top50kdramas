import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://en.wikipedia.org/wiki/Korean_drama'
    ]

    def parse(self, response):
        row = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/div[17]/ul/li[1]/table/tbody/tr')[1:]
        for i in range(len(row)):
            current_num = row[i].css('td::text').getall()
            current_link = row[i].css('a::text').getall()
            filler = current_link[1] if (
                row[i].get().count('td')) == 12 else filler

            yield {
                'rank': current_num[0],
                'title': current_link[0],
                'network': current_link[1] if (row[i]).get().count('td') == 12 else filler,
                'rating': current_num[1],
                'date': current_num[2]
            }
