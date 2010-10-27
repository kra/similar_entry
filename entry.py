from words import entry
import search
import util

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


class User(object):

    def __init__(self, username):
        self.username = username

    def recent_posts(self):
        """
        Return a sequence of recent posts.
        """
        return search.Search().user_search(self.username)


class Post(object):

    def __init__(self, text, user):
        self.text = text
        self.normalized_text = entry.String.normalized_words(self.text)
        self.user = user

    def combinations(self, min_words, max_words):
        """
        Yield all subsequences of normalized words from my text
        of length between min_words and max_words inclusive,
        in decreasing order of length.
        """
        w_len = min(len(self.normalized_text), max_words)
        while w_len >= min_words:
            for sub in combinations(self.normalized_text, w_len):
                if len(sub) <= max_words:
                    yield sub
            w_len -= 1

    def _qualified_post(self, post, min_words):
        """
        Return True if post qualfies as a similar post to myself.
        """
        if post.text.lower().find('rt ') == 0:
            return False
        if post.user.username != self.user.username:
            normalized_text = entry.String.normalized_words(
                post.text)
            if len(normalized_text) >= min_words:
                # we want a unique word in result or text
                if (set(normalized_text) != set(self.normalized_text)):
                    return True
        return False
        
    def find_similar(self, min_words, max_words):
        """
        Yield eligible seach results which match my text.
        """
        for words in self.combinations(min_words, max_words):
            for post in search.Search().search(words):
                if self._qualified_post(post, min_words):
                    yield post


if __name__ == '__main__':
    # test
    username = 'blaine'
    user = User(username)
    #print [
    #    post.text for post in Post(
    #        'friends please know how much', user).find_similar(3)]
    for post in user.recent_posts():
        util.log('post %s' % post.text)
        for similar_post in post.find_similar(4, 6):
            util.log('similar post %s' % similar_post.text)
