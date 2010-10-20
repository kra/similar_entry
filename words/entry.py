import stopwords
import string


class String(object):

    @classmethod
    def normalize_word(cls, word):
        """
        Return lowercased word without leading or trailing non-ascii.
        """
        word = word.lower()
        while word and word[0] not in string.ascii_lowercase:
            word = word[1:]
        while word and word[-1] not in string.ascii_lowercase:
            word = word[:-1]
        return word

    @classmethod
    def wanted_word(cls, word):
        """
        Return True if we want to keep this word.
        """
        if word.find('http:') != 0:
            if word not in stopwords.stopwords:
                return True
        return False
    
    @classmethod
    def normalized_words(cls, text):
        """
        Return normalized sequence of words from the_str.
        """
        words = [cls.normalize_word(word) for word in text.split()]
        words = [word for word in words if cls.wanted_word(word)]
        return words


class Entry(object):

    def __init__(self, user, text, min_words):
        self.user = user
        self.text = text
        self.min_words = min_words

    def find_similar(self):
        words = String.normalized_words(self.text)
        # search for each subset of words until we return a result or fail

    def search(self, words):
        """
        If the the normalized words of a result from a  search for words
        doesn't match words, return the result.
        """
        for result in search.Search(words):
            if set(String.normalized_words(result['text'])) != set(words):
                return result
