import unittest
import mox

import search


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.mox = mox.Mox()
        self.url_getter = self.mox.CreateMock(
            search.UrlGetter)

    def tearDown(self):
        self.mox.VerifyAll()        

    def test_search(self):
        self.url_getter.get(
            'http://search.twitter.com/search.json?q=scraper+bike+london'
            ).AndReturn("""{"results":[{"profile_image_url":"http://a2.twimg.com/profile_images/459762034/parrot_on_bike_normal.jpg","created_at":"Thu, 21 Oct 2010 10:37:34 +0000","from_user":"bikebot","metadata":{"result_type":"recent"},"to_user_id":null,"text":"RT @fastchicken @MalcolmBarclay I had a similar issue with London Bike App scraper. Put in a User Agent. That fixed it for me.","id":28014480878,"from_user_id":50323072,"geo":null,"iso_language_code":"en","source":"&lt;a href=&quot;http://twitterfeed.com&quot; rel=&quot;nofollow&quot;&gt;twitterfeed&lt;/a&gt;"},{"profile_image_url":"http://a2.twimg.com/profile_images/431209042/nic-twitter-pic_normal.jpg","created_at":"Thu, 21 Oct 2010 10:30:34 +0000","from_user":"fastchicken","metadata":{"result_type":"recent"},"to_user_id":2399095,"text":"@MalcolmBarclay I had a similar issue with London Bike App scraper. Put in a User Agent. That fixed it for me.","id":28014093014,"from_user_id":6801,"to_user":"MalcolmBarclay","geo":null,"iso_language_code":"en","source":"&lt;a href=&quot;http://twitter.com&quot; rel=&quot;nofollow&quot;&gt;Tweetie for Mac&lt;/a&gt;"}],"max_id":28443405825,"since_id":0,"refresh_url":"?since_id=28443405825&q=scraper+bike+london","total":2,"results_per_page":15,"page":1,"completed_in":0.295945,"query":"scraper+bike+london"}""")

        self.mox.ReplayAll()

        searcher = search.Search()
        searcher.url_getter = self.url_getter
        search_out = searcher.search(['scraper', 'bike', 'london'])
        self.assertEqual(len(search_out), 2)
        self.assertEqual(
            [entry['from_user'] for entry in search_out],
            ['bikebot', 'fastchicken'])


if __name__ == '__main__':
    unittest.main()
        
        
