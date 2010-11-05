import stopwords
import string


class String(object):

    @classmethod
    def normalize_word(cls, word):
        """
        Return lowercased word without leading or trailing non-ascii,
        if relevant, or None.
        """
        if not word:
            return None
        if word[0] == '@':
            return None
        if word[0] == '.':              # this is also used for RT
            return None
        word = word.lower()
        if word == 'rt':
            return None
        if word[0] == '&':
            # XML entity or starts with one, or whatevs
            return None
        while word and word[0] not in string.ascii_lowercase:
            word = word[1:]
        while word and word[-1] not in string.ascii_lowercase:
            word = word[:-1]
        if word.find('http:') == 0:
            return None
        if word in stopwords.stopwords:
            return None
        return word or None

    @classmethod
    def normalized_words(cls, text):
        """
        Return normalized sequence of words from the_str.
        """
        # XXX split on punctuation as well
        return [word for word in
                [cls.normalize_word(word) for word in text.split()]
                if word]
