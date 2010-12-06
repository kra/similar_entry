import config
import entry
import util

import operator
import datetime

def main():
    users = dict(
        [(name, entry.User(name)) for name in
         ['karlanderson',
          'blaine',
          'al3x',
          'nelson',
          'pennjillette',
          'theteller',
          'NASA_Ames',
          'ebertchicago',
          'hotdogsladies',
          'beatonna',
          'BPglobalPR',
          'tgammons',
          'jeresig',
          'uncleboatshoes',
          'mixedfeelings',
          'portlandmercury',
          'ourpdx',
          'CristopOConnor',
          'timbray',
          'FrontAve',
          'jennjoysmith',
          'brx0',
          'nothstine',
          'Paxochka',
          'erlsn',
          'tomtomorrow',
          'markos',
          'gabrielamadeus',
          'declanm',
          'lukedones',
          'kristyaudrey',
          'tlockney',
          'gfish',
          'queeniecarly',
          'adamd']])
    posts = {}

    while True:
        util.log('starting: posts:%s users:%s' % (len(posts), len(users)))
        # Ideally, we should be doing this asynchronously or something - always
        # be looking for new posts, always be looking for similar posts to what
        # we have.  Might need basic scheduling to do this right, though, want
        # to prioritize looking for similars for posts which haven't been
        # checked in a while.
        for user in users.values():
            for post in (
                post for post in user.recent_posts() if not post.is_rt()):
                if not posts.has_key(post.post_id):
                    posts[post.post_id] = post
            for post in sorted(posts.values(),
                key=operator.attrgetter('created_at')):
                if not post.responded_at:
                    util.log('post: %s %s %s' % (
                        post.created_at, post.from_user.username, post.text))
                    for similar_post in post.find_similar_entity_posts(
                        3, 3, 10, 2, config.calais_key):
                        util.log('similar: %s' % similar_post.text)
                        if not posts.has_key(similar_post.post_id):
                            posts[post.post_id] = post
                        if not users.has_key(similar_post.from_user.username):
                            users[similar_post.from_user.username] = (
                                similar_post.from_user)
                 
                        post.responded_at = datetime.datetime.utcnow()
                                
if __name__ == '__main__':
    main()
