import unittest


class TestAreAnagrams(unittest.TestCase):
    def test_areanagrams_vide(self):
        self.assertEqual(are_anagrams('', ''), False)

    def test_areanagrams_a_a(self):
        self.assertEqual(are_anagrams('a', 'a'), True)

    def test_areanagrams_vide_a(self):
        self.assertEqual(are_anagrams('', 'a'), False)

    def test_areanagrams_ba_ab(self):
        self.assertEqual(are_anagrams('ba', 'ab'), True)

    def test_areanagrams_ba_vide(self):
        self.assertEqual(are_anagrams('ba', ''), False)


def are_anagrams(word_a: str, word_b: str):
    if len(word_a) > 0 and len(word_b) > 0:
        if word_a[0] == word_b[-1]:
            return True
    return False


if __name__ == '__main__':
    unittest.main()
