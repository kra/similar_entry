import stopwords
import string


class String(object):

    def __init__(self, the_str):
        self.str = the_str

    def normalize_word(self, word):
        """
        Return word without leading or trailing non-ascii.
        """
        word = word.lower()
        while word and word[0] not in string.ascii_lowercase:
            word = word[1:]
        while word and word[-1] not in string.ascii_lowercase:
            word = word[:-1]
        return word

    def normalized_words(self, the_str):
        """
        Return normalized sequence of words from the_str.
        """
        words = [self.normalize_word(word) for word in the_str.split()]
        words = [word for word in words if word.find('http:') != 0]
        return [word for word in words if word not in stopwords.stopwords]
