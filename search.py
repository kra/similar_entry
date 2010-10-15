import urllib
import simplejson


class Search(object):

    @classmethod
    def search_url(cls, words):
        """
        Return a URL for a search for words with JSON output.
        """
        return 'http://search.twitter.com/search.json?q=%s' % ('+'.join(words))

    @classmethod
    def search_results(cls, result_string):
        """
        Return a sequence of relevant attributes from result_string.
        """
        return [{'from_user':result['from_user'],
                 'text':result['text']}
                for result in simplejson.loads(result_string)['results']]

    @classmethod
    def search(cls, words):
        """
        Return the results of a search for words.
        """
        return cls.search_results(urllib.urlopen(cls.search_url(words)).read())


if __name__ == '__main__':
    # test
    print Search.search(['friends', 'please'])
