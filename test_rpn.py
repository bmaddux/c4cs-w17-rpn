import unittest
import rpn
class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
	def test_multiply(self):
		result = rpn.calculate('2 7 *')
		self.assertEqual(14, result)
	def test_divide(self):
		result = rpn.calculate('16 8 /')
		self.assertEqual(2, result)
	def test_exponent(self):
		result = rpn.calculate('2 5 ^')
		self.assertEqual(32, result)