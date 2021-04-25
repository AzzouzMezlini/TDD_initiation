import unittest


class TestAreAnagrams(unittest.TestCase):
    def test_areanagrams(self):
        self.assertEqual(are_anagrams(), False)


def are_anagrams():
    return False


if __name__ == '__main__':
    unittest.main()
