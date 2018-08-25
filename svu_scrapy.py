import scrapy
import re
from ..items import EpisodeItem, CastItem

class SvuSpider(scrapy.Spider):
    name = "svu"
    start_urls = [
        'https://www.imdb.com/title/tt0629700/?ref_=ttep_ep1'
    ]

    def parse(self, response):
        # Gather episode information
        item = EpisodeItem(
            season = response.xpath("//div[@class='bp_heading']/text()")[0].extract(),
            episode = response.xpath("//div[@class='bp_heading']/text()")[1].extract(),
            episode_name = response.xpath("//h1[@itemprop='name']/text()").extract_first().strip(),
            date_published = response.xpath("//div[@class='subtext']/a/meta[@itemprop='datePublished']/@content").extract(),
            rating_value = response.xpath("//span[@itemprop='ratingValue']/text()").extract(),
            rating_count = response.xpath("//span[@itemprop='ratingCount']/text()").extract()
        )
        yield item

        # Follow link to full cast list
        for a in response.xpath("//div[@class='see-more']/a"):
            yield response.follow(a, callback=self.parse_cast)

        # Follow link to next episode
        for a in response.xpath("//a[@class='bp_item np_next']"):
            yield response.follow(a, callback=self.parse)

    def parse_cast(self, response):
        # Gather cast list data
        for castmember in response.xpath("//table[@class='cast_list']"):

            character = castmember.xpath("//td[@class='character']/a/text() | //td[@class='character']/text()").extract()
            #character = [re.sub(r'^\s*$', 'NA', c) for c in character]
            character = [re.sub(r'\(.*\)', '', c) for c in character if c.strip()]
            character = [c.strip().replace('\n ', '') for c in character if c.strip()]
            item = CastItem(
                episode_name = castmember.xpath("//h3[@itemprop='name']/a/text()").extract_first().strip(),
                actor = castmember.xpath("//td[@itemprop='actor']/a/span[@itemprop='name']/text()").extract(),
                character = character
            )
            yield item
