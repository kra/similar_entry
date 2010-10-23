from words import entry
import search

# This is in python2.6 itertools, copied from the lib docs.
def combinations(iterable, r):
    """
    Yield all subsequences of iterable of length r.
    If elements of iterable are unique, these are subsets.
    """
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


class Entry(object):

    def __init__(self, text, min_words, user):
        self.text = text
        self.min_words = min_words
        self.max_words = 10             # max words we can search for
        self.user = user

    def combinations(self):
        """
        Yield all subsequences of normalized words from my text
        of length between my min_words and max_words inclusive,
        in decreasing order of length.
        """
        words = entry.String.normalized_words(self.text)
        w_len = min(len(words), self.max_words)
        while w_len >= self.min_words:
            for sub in combinations(words, w_len):
                if len(sub) <= self.max_words:
                    yield sub
            w_len -= 1
        
    def find_similar(self):
        """
        Yield eligible seach results which match my text.
        """
        for words in self.combinations():
            for result in search.Search().search(words):
                if result['from_user'] != self.user:
                    normalized_text = entry.String.normalized_words(
                        result['text'])
                    if len(normalized_text) >= self.min_words:
                        # we want a unique word in result or text
                        if (set(normalized_text) != set(words)):
                            yield result


if __name__ == '__main__':
    # test
    print [
        result for result in Entry(
            'friends please know how much', 3, 'user').find_similar()]
