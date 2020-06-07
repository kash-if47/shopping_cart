import unittest
from dataclasses import dataclass
from typing import List

from shopping_cart import Basket


class MyTestCase(unittest.TestCase):
    def test_something(self):
        basket = Basket([])
        self.assertEqual(basket.total(), 0)

    def test_single_item(self):
        basket = Basket(['Cake'])
        self.assertEqual(basket.total(), 1)

if __name__ == '__main__':
    unittest.main()
