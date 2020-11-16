from scrapy import Item, Field


class TopicItem(Item):
    url = Field()
    title = Field()
    author = Field()  

class ContentItem(Item):
    url = Field()
    content = Field()
    author = Field()  