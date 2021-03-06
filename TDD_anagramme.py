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

    def test_areanagrams_ba_bc(self):
        self.assertEqual(are_anagrams('ba', 'bc'), False)

    def test_areanagrams_bac_bc(self):
        self.assertEqual(are_anagrams('bac', 'bc'), False)

    def test_areanagrams_bac_cb(self):
        self.assertEqual(are_anagrams('bac', 'cb'), False)

    def test_areanagrams_bac_acb(self):
        self.assertEqual(are_anagrams('bac', 'acb'), True)

    def test_areanagrams_abc_acb(self):
        self.assertEqual(are_anagrams('abc', 'acb'), True)

    def test_areanagrams_abcd_adcb(self):
        self.assertEqual(are_anagrams('abcd', 'adcb'), True)

    def test_areanagrams_transfusion_fournissant (self):
        self.assertEqual(are_anagrams('transfusion', 'fournissant'), True)

    def test_areanagrams_transfusion_fournissant (self):
        self.assertEqual(are_anagrams('transfusion', 'transfusiez'), False)


def are_anagrams(word_a: str, word_b: str):
    if len(word_a) == len(word_b) > 0:
        for letter in word_b:
            if not word_a.__contains__(letter):
                return False
        return True
    return False


if __name__ == '__main__':
    unittest.main()
