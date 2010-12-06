import unittest

import entry


class TestEntry(unittest.TestCase):

    def test_module_combinations(self):
        self.assertEqual(
            [x for x in entry.combinations([1,2,3], 4)], [])
        self.assertEqual(
            [x for x in entry.combinations([1,2,3], 3)],
            [(1,2,3)])
        self.assertEqual(
            [x for x in entry.combinations([1,2,3], 2)],
            [(1,2), (1,3), (2,3)])
        self.assertEqual(
            [x for x in entry.combinations([1,2,3], 1)],
            [(1,), (2,), (3,)])

    def test_combinations(self):
        post = entry.Post(
            'foo bar baz', entry.User('username'), 666,
            "Sun, 31 Oct 2010 03:04:21 +0000")
        self.assertEqual(
            [x for x in post.word_combinations(4, 10)],
            [])
        self.assertEqual(
            [x for x in post.word_combinations(3, 10)],
            [('foo', 'bar', 'baz')])
        self.assertEqual(
            [x for x in post.word_combinations(2, 10)],
            [('foo', 'bar', 'baz'),
             ('foo', 'bar'), ('foo', 'baz'), ('bar', 'baz')])
        self.assertEqual(
            [x for x in post.word_combinations(1, 10)],
            [('foo', 'bar', 'baz'),
             ('foo', 'bar'), ('foo', 'baz'), ('bar', 'baz'),
             ('foo',), ('bar',), ('baz',)])

    def test_usernames(self):
        self.assertEqual(
            entry.Post('', entry.User('username'), 666,
                       "Sun, 31 Oct 2010 03:04:21 +0000")._usernames(),
            set(['username']))
        self.assertEqual(
            entry.Post('foo bar baz', entry.User('username'), 666,
                       "Sun, 31 Oct 2010 03:04:21 +0000")._usernames(),
            set(['username']))
        self.assertEqual(
            entry.Post('@foo @bar baz @qux', entry.User('username'), 666,
                       "Sun, 31 Oct 2010 03:04:21 +0000")._usernames(),
            set(['username', 'foo', 'bar', 'qux']))

    def test_is_rt(self):
        self.assertEqual(
            entry.Post('', entry.User('username'), 666,
                       "Sun, 31 Oct 2010 03:04:21 +0000").is_rt(), False)
        self.assertEqual(
            entry.Post('RT @foo bar', entry.User('username'), 666,
                       "Sun, 31 Oct 2010 03:04:21 +0000").is_rt(), True)
        self.assertEqual(
            entry.Post('foo RT @foo bar', entry.User('username'), 666,
                       "Sun, 31 Oct 2010 03:04:21 +0000").is_rt(), True)
        self.assertEqual(
            entry.Post(' .@foo bar', entry.User('username'), 666,
                       "Sun, 31 Oct 2010 03:04:21 +0000").is_rt(), True)
        self.assertEqual(
            entry.Post('.@foo bar', entry.User('username'), 666,
                       "Sun, 31 Oct 2010 03:04:21 +0000").is_rt(), True)

if __name__ == '__main__':
    unittest.main()
