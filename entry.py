from words import entry
import search
import util
import calais_util

import datetime
import re

# This is in python2.6 itertools, copied from the lib docs.
# If elements of iterable are unique, these are subsets.
def combinations(iterable, r):
    """
    Yield all subsequences of iterable of length r.
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

def all_combinations(iterable, min_elts, max_elts):
    """
    Yield all subsequences of iterable of length min_elts to max_elts
    inclusive, in decreasing order of length.
    """
    while max_elts >= min_elts:
        for sub in combinations(iterable, max_elts):
            yield sub
        max_elts -= 1
    

class User(object):

    def __init__(self, username):
        self.username = username

    def recent_posts(self):
        """
        Return a sequence of recent posts.
        """
        return search.Search().user_search(self.username)


class Post(object):

    def __init__(self, text, from_user, post_id, created_at):
        self.text = text
        self.normalized_text = entry.String.normalized_words(self.text)
        self.from_user = from_user
        self.post_id = post_id
        self.created_at = datetime.datetime.strptime(
            created_at, '%a, %d %b %Y %H:%M:%S +0000')
        self.responded_at = None

    def word_combinations(self, min_words, max_words):
        """
        Yield all subsequences of normalized words from my text
        of length between min_words and max_words inclusive,
        in decreasing order of length.
        """
        return all_combinations(
            self.normalized_text,
            min_words, min(len(self.normalized_text), max_words))

    def _qualified_post_text(self, post, min_words):
        """
        Return True if text of post qualfies as a similar post to myself.
        """
        if post.text.strip().lower().find('rt ') == 0:
            return False
        if len(post.normalized_text) < min_words:
            return False
        return True

    def _usernames(self):
        """
        Return a set of relevent usernames.
        """
        return set(re.findall('@([\w]+)', self.text) + [
            self.from_user.username])

    def is_rt(self):
        """
        Return True if I am an RT.
        """
        for pattern in ('^@', '.@'):
            if self.text.find(pattern) > -1:
                return True
        if re.match('rt[\W]*@', self.text, re.IGNORECASE):
            return True
        if re.search('[\W]+rt[\W]*@', self.text, re.IGNORECASE):
            return True
        return False

    def _qualified_post(self, post, min_words, min_diff):
        """
        Return True if post qualfies as a similar post to myself.
        """
        # disqualify if posts both mention a user, or each others' users
        if self._usernames().intersection(post._usernames()):
            return False
        if post.is_rt():
            return False
        if post.from_user.username != self.from_user.username:
            if self._qualified_post_text(post, min_words):
                # we want unique words in result or text
                if (len(set(post.normalized_text).symmetric_difference(
                    set(self.normalized_text))) >= min_diff):
                    return True
        return False
        
    def find_similar_word_posts(self, min_words, max_words, min_diff):
        """
        Yield eligible seach results which match my text.
        """
        for words in self.word_combinations(min_words, max_words):
            for post in search.Search().search(words):
                if self._qualified_post(post, min_words, min_diff):
                    yield post
        
    def find_similar_entity_posts(
        self, min_entities, min_words, max_words, min_diff, calais_key):
        """
        Yield eligible seach results with words which match
        entries from my text of max_words or less.
        """
        # XXX add all URLs, calais doesn't like them all for some reason
        entities = calais_util.get_entities(self.text, calais_key)
        util.log('entities: %s' % entities)
        for combo in all_combinations(
            entities, min_entities, len(entities)):
            words = ' '.join(combo).split()
            if len(' '.join(combo).split()) <= max_words:
                for post in search.Search().search(words):
                    if self._qualified_post(post, min_words, min_diff):
                        yield post
        

if __name__ == '__main__':
    # test
    import config
    username = 'al3x'#'blaine'
    user = User(username)
    for post in (post for post in user.recent_posts() if not post.is_rt()):
        util.log('post: %s' % post.text)
        #for similar_post in post.find_similar_word_posts(4, 6):
        #    util.log('similar: %s' % similar_post.text)
        for similar_post in post.find_similar_entity_posts(
            3, 3, 10, 2, config.calais_key):
            util.log('similar: %s' % similar_post.text)
