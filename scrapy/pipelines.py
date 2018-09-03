# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import signals
from scrapy.exporters import CsvItemExporter

from .items import CastItem, EpisodeItem

class IMDBPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        item_names = ['episode', 'cast']
        self.files = self.files = {n: open('%s.csv' % n, 'w+b') for n in item_names}
        self.exporters = {n: CsvItemExporter(f) for n, f in self.files.items()}
        for exporter in self.exporters.values():
            exporter.start_exporting()

    def spider_closed(self, spider):
        for exporter in self.exporters.values():
            exporter.finish_exporting()

        for file in self.files.values():
            file.close()

    def process_item(self, item, spider):
        if isinstance(item, EpisodeItem):
            self.exporters['episode'].export_item(item)

        if isinstance(item, CastItem):
            self.exporters['cast'].export_item(item)

        return item
