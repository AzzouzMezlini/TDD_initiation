import unittest


class TestAreAnagrams(unittest.TestCase):
    def test_areanagrams(self):
        self.assertEqual(are_anagrams('', ''), False)


def are_anagrams(word_a: str, word_b: str):
    return False


if __name__ == '__main__':
    unittest.main()
