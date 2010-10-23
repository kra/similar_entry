import urllib2
import simplejson


class UrlGetter(object):
    @classmethod
    def get(cls, url):
        try:
            return urllib2.urlopen(url).read()
        except urllib2.URLError, exc:
            # want to back off and retry if this exc.code indicates throttling
            raise NotImplementedError
        

class Search(object):

    url_getter = UrlGetter

    def _search_url(self, words):
        """
        Return a URL for a search for words with JSON output.
        """
        return 'http://search.twitter.com/search.json?q=%s' % ('+'.join(words))

    def _search_results(self, result_string):
        """
        Return a sequence of relevant attributes from result_string.
        """
        return [{'from_user':result['from_user'],
                 'text':result['text']}
                for result in simplejson.loads(result_string)['results']]

    def search(self, words):
        """
        Return the results of a search for words.
        """
        return self._search_results(
            self.url_getter.get(self._search_url(words)))
    
        
if __name__ == '__main__':
    # test
    #print Search().search(['now','is','the','time','for','all','good','men','to','aid','boo'])
    print Search().search(['now','is','the','time'])
