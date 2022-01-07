import scrapy
from ..items import HolidaysItem


class holi(scrapy.Spider):
    name = "holiday"
    start_urls=[
        "https://www.officeholidays.com/countries/india/2021"
                ]
    def parse(self,response):
        items = HolidaysItem()

        all_code = response.css("tr.region")

        for i in all_code:


            Day =i.css("td::text").extract()
            Date = i.css("time::text").extract()
            Holiday_name = i.css(".country-listing::text").extract()
            Type = i.css(".comments::text").extract()
            comments = i.css(".hide-ipadmobile::text").extract()

            items['Day'] = Day[0]
            items['Date']= Date
            items['Holiday_name']= Holiday_name
            items['Type']= Type
            items['comments']= comments


            yield  items