import config
import entry
import util
import storage

import datetime

def main():
    posts = storage.Posts()    
    users = storage.Users()
    for name in [
        'karlanderson',
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
        'adamd']:
        users.create(entry.User(name))

    while True:
        util.log('starting: posts:%s users:%s' % (len(posts), len(users)))
        # Ideally, we should be doing this asynchronously or something - always
        # be looking for new posts, always be looking for similar posts to what
        # we have.  Might need basic scheduling to do this right, though, want
        # to prioritize looking for similars for posts which haven't been
        # checked in a while.
        for user in users.get_all():
            for post in (
                post for post in user.recent_posts() if not post.is_rt()):
                posts.create(post)
            for post in posts.get_all('created_at'):
                if not post.responded_at:
                    util.log('post: %s %s %s' % (
                        post.created_at, post.from_user.username, post.text))
                    for similar_post in post.find_similar_entity_posts(
                        3, 3, 10, 2, config.calais_key):
                        util.log('similar: %s' % similar_post.text)
                        posts.create(similar_post)
                        users.create(similar_post.from_user)
                        post.responded_at = datetime.datetime.utcnow()
                                
if __name__ == '__main__':
    main()
