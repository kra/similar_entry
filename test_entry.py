import unittest
import entry


class TestString(unittest.TestCase):

    def test_normalize(self):
        s = entry.String()
        for (str_in, str_out) in [
            ('foo', 'foo'),
            ('9foo9bar9', 'foo9bar'),
            ('@', ''),
            ('', ''),
            ]:
            self.assertEqual(s.normalize(str_in), str_out)


if __name__ == '__main__':
    unittest.main()
