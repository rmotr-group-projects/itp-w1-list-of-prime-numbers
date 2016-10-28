import unittest

from list_of_prime_numbers import list_of_prime_numbers
from list_of_prime_numbers.main import _is_prime


class TestIsPrime(unittest.TestCase):
    def test_big_number_prime_true(self):
        self.assertEqual(_is_prime(19), True)

    def test_big_number_prime_false(self):
        self.assertEqual(_is_prime(20), False)

    def test_one_prime(self):
        self.assertEqual(_is_prime(1), False)

    def test_two_prime(self):
        self.assertEqual(_is_prime(2), True)

    def test_three_prime(self):
        self.assertEqual(_is_prime(3), True)

    def test_four_prime(self):
        self.assertEqual(_is_prime(4), False)


class TestListOfPrimeNumbers(unittest.TestCase):
    def test_big_number_list(self):
        self.assertEqual(
            list_of_prime_numbers(19),
            [2, 3, 5, 7, 11, 13, 17, 19])

    def test_list_one(self):
        self.assertEqual(list_of_prime_numbers(1), [])

    def test_list_zero(self):
        self.assertEqual(list_of_prime_numbers(0), [])
