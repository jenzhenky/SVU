# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class EpisodeItem(Item):
    season = Field()
    episode = Field()
    episode_name = Field()
    date_published = Field()
    rating_value = Field()
    rating_count = Field()

class CastItem(Item):
    episode_name = Field()
    actor = Field()
    character = Field()
    cast_ranking = Field()
