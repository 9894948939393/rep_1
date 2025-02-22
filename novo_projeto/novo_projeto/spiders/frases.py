import scrapy
import json

class MeuSpider(scrapy.Spider):
    name = "frases"
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        dados = []
        for quote in response.css("div.quote"):
            item = {
                "autor": quote.css("small.author::text").get(),
                "texto": quote.css("span.text::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
            dados.append(item)

        with open("dados.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
