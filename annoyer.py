recent_delta = 60 * 60 * 24 * 666       # how far back to search
min_words = 666


class User:
    def recent_tweets(self, delta):
        "Yield tweets from user later than delta."
        raise NotImplementedError

    def following(self, followed_user):
        "Return True if user follows followed_user."
        raise NotImplementedError


def get_user():
    """
    Yield a User.
    """
    raise NotImplementedError

# skip users:
# sender of tweet we're trying to match
# user who sender follows
def matching_tweets(words, min_words, start_delta, end_delta, skip_users=[]):
    """
    Yield tweets which match at least min_words of words, unordered, are
    not from skip_users, and were sent between start_delta before now and
    end_delta before now.
    """
    raise NotImplementedError

user = get_user().next()
tweets = user.recent_tweets(recent_delta)
for tweet in tweets:
    words = tweet.tweet_str.normalized_words()
    if len(words) >= min_words:
        pass
        
        

