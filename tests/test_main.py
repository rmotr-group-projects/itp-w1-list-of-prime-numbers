# -*- coding: utf-8 -*-
import unittest

from list_of_prime_numbers import main


class TestListOfPrimeNumbers(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(1 + 1, 2)
