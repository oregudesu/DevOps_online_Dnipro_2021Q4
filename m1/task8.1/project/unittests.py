import unittest
from main import discriminant, roots, solv_square 


class TestSquareEquasionApp(unittest.TestCase):
	def test_discriminant(self):
		result = discriminant(a=1, b=-6, c=9)
		expected_result = 0
		self.assertEqual(result, expected_result)
		
	def test_roots(self):
		result = roots(d=4, a=1, b=-6, c=8)
		expected_result = [2, 4]
		self.assertEqual(result, expected_result)
		
	def test_solv_square(self):
		result = solv_square(a=1, b=1, c=5)
		expected_result = []
		self.assertEqual(result, expected_result)
		

if __name__ == "__main__":
	unittest.main()

