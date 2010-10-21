from words import entry
import search


class Entry(object):

    def __init__(self, user, text, min_words):
        self.user = user
        self.text = text
        self.min_words = min_words

    def find_similar(self):
        """
        Yield eligible seach results which match my text.
        """
        words = entry.String.normalized_words(self.text)
        for result in search.Search.search(words):
            normalized_result = entry.String.normalized_words(result['text'])
            if len(normalized_result) < self.min_words:
                continue
            if (set(normalized_result) != set(words)):
                # we want a unique word in result or text
                continue
            yield result


if __name__ == '__main__':
    # test
    print [
        result for result in Entry(
            'dummy', 'friends please know how much', 3).find_similar()]
