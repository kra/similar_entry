"""
Demo collection classes, to be replaced by a real storage someday.
"""

import operator


class Users:
    """
    Collection class for User models, indexed by usernaeme.
    """

    def __init__(self):
        self._users = {}
    
    def create(self, user):
        """
        Add user, do nothing if alrady existing.
        """
        if not self._users.has_key(user.username):
            self._users[user.username] = user

    def get_all(self):
        """
        Return a generator of all users.
        """
        #return self._users.itervalues()
        return (post for post in self._users.values())

    def __len__(self):
        return len(self._users)
    

class Posts:
    """
    Storage for Post models, indexed by post_id
    """
    def __init__(self):
        self._posts = {}
    
    def create(self, post):
        """
        Add post, do nothing if already existing.
        """
        if not self._posts.has_key(post.post_id):
            self._posts[post.post_id] = post

    def get_all(self, sort_attr=None):
        """
        Return a generator of all posts.
        """
        if not sort_attr:
            return (post for post in self._posts.values())
        return (post for post in sorted(
            self._posts.values(), key=operator.attrgetter(sort_attr)))

    def __len__(self):
        return len(self._posts)
    
