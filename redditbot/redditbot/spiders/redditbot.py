import scrapy
from redditbot.items import RedditbotItem
from datetime import datetime
import re


class Redditbot(scrapy.Spider):
    name = "redditbot"

    # Url inicial
    start_urls = ["https://fundrazr.com/find?category=Health"]


    # Troca de pagina
    for i in range(2, 4):
        start_urls.append("https://fundrazr.com/find?category=Health&page=" + str(i) + "")

    def parse(self, response):
        for href in response.xpath(
                "//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href"):
            url = "https:" + href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = RedditbotItem()

        # Titulo da camapanha
        item['tituloCampanha'] = response.xpath("//div[contains(@id, 'campaign-title')]/descendant::text()").extract()[
            0].strip()

        # Total arrecadado
        item['arrecadado'] = response.xpath(
            "//span[contains(@class, 'stat')]/span[contains(@class, 'amount-raised')]/descendant::text()").extract()

        # Objetivo a ser arrecadado
        item['objetivo'] = " ".join(response.xpath(
            "//div[contains(@class, 'stats-primary with-goal')]//span[contains(@class, 'stats-label hidden-phone')]/text()").extract()).strip()

        # Moeda
        item['moeda'] = response.xpath("//div[contains(@class, 'stats-primary with-goal')]/@title").extract()

        # Encerramento da campanha
        item['encerramento'] = "".join(response.xpath(
            "//div[contains(@id, 'campaign-stats')]//span[contains(@class,'stats-label hidden-phone')]/span[@class='nowrap']/text()").extract()).strip()

        # Total de contribuidores
        item['contribuidores'] = response.xpath(
            "//div[contains(@class, 'stats-secondary with-goal')]//span[contains(@class, 'donation-count stat')]/text()").extract()

        # Historia
        historias = response.xpath("//div[contains(@id, 'full-story')]/descendant::text()").extract()
        historias = [x.strip() for x in historias if len(x.strip()) > 0]
        item['historia'] = " ".join(historias)

        # Url
        item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()

        yield item
