# test di une chaine de caratère est un Palindrome
import unittest


class TestStringMethods(unittest.TestCase):

    def test_vide(self):
        self.assertEqual(is_palindrome(''), False)

    def test_a(self):
        self.assertEqual(is_palindrome('a'), False)

    def test_aa(self):
        self.assertEqual(is_palindrome('aa'), True)

    def test_aba(self):
        self.assertEqual(is_palindrome('aba'), True)

    def test_abca(self):
        self.assertEqual(is_palindrome('abca'), False)

    def test_abba(self):
        self.assertEqual(is_palindrome('abba'), True)

    def test_racecar(self):
        self.assertEqual(is_palindrome('racecar'), True)

    def test_table(self):
        self.assertEqual(is_palindrome('table'), False)

    def test_RaceCar(self):
        self.assertEqual(is_palindrome('RaceCar'), False)


def is_palindrome(aword: str):
    if len(aword) > 1:
        for index, letter in enumerate(aword):
            if letter != aword[-(index + 1)]:
                return False
        return True
    return False

if __name__ == '__main__':
    unittest.main()
