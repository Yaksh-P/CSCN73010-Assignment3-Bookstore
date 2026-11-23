import unittest

from src.bookstore import quote


class QuoteTests(unittest.TestCase):
    def test_two_python_books(self):
        self.assertEqual(quote("python", 2), 5000)

    def test_unknown_book(self):
        with self.assertRaisesRegex(ValueError, "Unknown book"):
            quote("missing", 1)

    def test_negative_quantity(self):
        with self.assertRaisesRegex(ValueError, "Quantity must be positive"):
            quote("python", -1)
