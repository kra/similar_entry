import urllib2
import simplejson
import entry
import time

def log(msg): print msg


class UrlGetter(object):
    sleep_secs = 'xxx'
    @classmethod
    def get(cls, url):
        cls.sleep_secs = 0.125
        while True:
            # Q&d backing off in response to throttling.
            # This works if there's one single-threaded UrlGetter.
            time.sleep(cls.sleep_secs)
            try:
                out = urllib2.urlopen(url).read()
                # this is probably susceptible to rounding errors
                cls.sleep_secs /= 2
                return out
            except urllib2.URLError, exc:
                if exc.code == 420:
                    cls.sleep_secs *= 2
                    log('UrlGetter sleeping %s' % cls.sleep_secs)
                

class Search(object):

    url_getter = UrlGetter

    def _search_url(self, words):
        """
        Return a URL for a search for words with JSON output.
        """
        return 'http://search.twitter.com/search.json?q=%s' % ('+'.join(words))

    def _user_search_url(self, username):
        """
        Return a URL for a search for username with JSON output.
        """
        return 'http://search.twitter.com/search.json?q=from%%3A%s' % username

    def _search_results(self, result_string):
        """
        Return a sequence of posts.
        """
        return [
            entry.Post(result['text'], entry.User(result['from_user']))
            for result in simplejson.loads(result_string)['results']]

    def search(self, words):
        """
        Return the results of a search for words.
        """
        return self._search_results(
            self.url_getter.get(self._search_url(words)))

    def user_search(self, username):
        """
        Return the results of a search for username.
        """
        return self._search_results(
            self.url_getter.get(self._user_search_url(username)))
    
        
if __name__ == '__main__':
    # test
    print Search().search(['now','is','the','time'])
