from lassie import Lassie

from urlparse import urlparse
import unittest


class FakeLassie(Lassie):
    def _retreive_content(self, url):
        filename = urlparse(url).path
        file = open('./templates/%s' % filename, 'r')
        html = file.read()
        file.close()

        return html


class LassieTwitterCardTestCase(unittest.TestCase):
    def setUp(self):
        self.api = FakeLassie()

    def test_twitter_all_properties(self):
        data = self.api.fetch(url='http://lassie.it/twitter/all_properties.html')
        self.assertEqual(data['url'], 'http://www.youtube.com/watch?v=fWNaR-rxAic')
        self.assertEqual(data['title'], 'Carly Rae Jepsen - Call Me Maybe')
        self.assertEqual(data['description'], 'Buy Now! http://smarturl.it/CallMeMaybe Music video by Carly Rae Jepsen performing Call Me Maybe. (C) 2011 604 Records Inc. #VEVOCertified on June 8, 2012. h...')

        self.assertEqual(len(data['images']), 1)
        image = data['images'][0]
        self.assertEqual(image['src'], 'http://i1.ytimg.com/vi/fWNaR-rxAic/maxresdefault.jpg')