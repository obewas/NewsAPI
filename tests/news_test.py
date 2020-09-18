import unittest
from app.models import news
News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News("abd-news", "ABC News", "Trusted source", 'https://abcnews.go.com', "general", "en", "us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))


