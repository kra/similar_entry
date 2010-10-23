import unittest
import words.entry


class TestString(unittest.TestCase):

    def test_normalize_word(self):
        for (str_in, str_out) in [
            ('foo', 'foo'),
            ('9foo9bar!!', 'foo9bar'),
            ('@', ''),
            ('@foo', 'foo'),            
            ('', ''),
            ]:
            self.assertEqual(
                words.entry.String.normalize_word(str_in), str_out)

    def test_wanted_word(self):
        self.assertTrue(words.entry.String.wanted_word('foo'))
        for word in ('the', 'http://example.org'):
            self.assertFalse(words.entry.String.wanted_word(word))


if __name__ == '__main__':
    unittest.main()
