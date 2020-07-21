# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyspiderPipeline:
    def process_item(self, item, spider):
        movies_list = []
        title = item['title']
        film_type = item['film_type']
        film_time = item['film_time']
        # output = f'|{title}|\t|{film_type}|\t|{film_time}|\n\n'
        movies_list.append([title, film_type, film_time])
        import pandas as pd
        # with open('./maoyanmovie.csv', 'a+', encoding='utf-8') as article:
        df = pd.DataFrame(data=movies_list)
        df.to_csv("./maoyanmovie.csv", encoding="utf-8-sig", mode="a+", header=False, index=False)

        return item
