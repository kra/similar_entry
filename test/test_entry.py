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
        user = entry.User('username')
        self.assertEqual(
            [x for x in entry.Post('foo bar baz', user).combinations(4, 10)],
            [])
        self.assertEqual(
            [x for x in entry.Post('foo bar baz', user).combinations(3, 10)],
            [('foo', 'bar', 'baz')])
        self.assertEqual(
            [x for x in entry.Post('foo bar baz', user).combinations(2, 10)],
            [('foo', 'bar', 'baz'),
             ('foo', 'bar'), ('foo', 'baz'), ('bar', 'baz')])
        self.assertEqual(
            [x for x in entry.Post('foo bar baz', user).combinations(1, 10)],
            [('foo', 'bar', 'baz'),
             ('foo', 'bar'), ('foo', 'baz'), ('bar', 'baz'),
             ('foo',), ('bar',), ('baz',)])


if __name__ == '__main__':
    unittest.main()
