import config
import entry
import util

import operator
import datetime

def main():
    users = {'karlanderson':entry.User('karlanderson'),
             'blaine':entry.User('blaine'),
             'al3x':entry.User('al3x'),
             'nelson':entry.User('nelson'),
             'pennjilette':entry.User('pennjilette'),
             'theteller':entry.User('theteller')             
             }
    posts = {}

    while True:
        util.log('starting: posts:%s users:%s' % (len(posts), len(users)))
        for user in users.values():
            for post in user.recent_posts():
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
                        import pdb; pdb.set_trace()
                        if not users.has_key(similar_post.from_user.username):
                            users[similar_post.from_user.username] = (
                                similar_post.from_user)
                 
                        post.responded_at = datetime.datetime.utcnow()
                                
if __name__ == '__main__':
    main()
