import unittest
import words.entry


class TestString(unittest.TestCase):

    def test_normalize_word(self):
        for (str_in, str_out) in [
            ('foo', 'foo'),
            ('9foo9bar!!', 'foo9bar'),
            ('@', None),
            ('@foo', None),            
            ('', None),
            ('the', None),            
            ]:
            self.assertEqual(
                words.entry.String.normalize_word(str_in), str_out)


if __name__ == '__main__':
    unittest.main()
