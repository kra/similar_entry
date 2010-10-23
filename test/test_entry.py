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
        self.assertEqual(
            [x for x in entry.Entry('foo bar baz', 4, 'user').combinations()],
            [])
        self.assertEqual(
            [x for x in entry.Entry('foo bar baz', 3, 'user').combinations()],
            [('foo', 'bar', 'baz')])
        self.assertEqual(
            [x for x in entry.Entry('foo bar baz', 2, 'user').combinations()],
            [('foo', 'bar', 'baz'),
             ('foo', 'bar'), ('foo', 'baz'), ('bar', 'baz')])
        self.assertEqual(
            [x for x in entry.Entry('foo bar baz', 1, 'user').combinations()],
            [('foo', 'bar', 'baz'),
             ('foo', 'bar'), ('foo', 'baz'), ('bar', 'baz'),
             ('foo',), ('bar',), ('baz',)])


if __name__ == '__main__':
    unittest.main()
