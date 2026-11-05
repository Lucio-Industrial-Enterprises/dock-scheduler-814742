import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_service(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)
        self.assertEqual(shipping_quote(2, "regional", service="standard"), 11.0)

    def test_express_rates(self):
        # express = standard + $7
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_different_weights(self):
        self.assertEqual(shipping_quote(1, "local", service="express"), 13.5)
        self.assertEqual(shipping_quote(10, "regional", service="express"), 30.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
