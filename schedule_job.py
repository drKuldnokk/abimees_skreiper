from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:7556')
scrapyd.schedule('kratt', 'providers', search_word="kodukino", location="Harjumaa")