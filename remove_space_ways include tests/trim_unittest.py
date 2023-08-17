import unittest
import remove_space_by_slice


class TestTrim(unittest.TestCase):
    def test_behind_space(self):
        self.assertEqual(remove_space_by_slice.trim('hello python '), 'hello python '.strip())

    def test_front_space(self):
        self.assertEqual(remove_space_by_slice.trim(' hello python'), ' hello python'.strip())

    def test_sides_space(self):
        self.assertEqual(remove_space_by_slice.trim(' hello python '), ' hello python '.strip())

    def test_multiple_sides_space(self):
        self.assertEqual(remove_space_by_slice.trim('  hello python  '), '  hello python  '.strip())


if __name__ == '__main__':
    unittest.main()
