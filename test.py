import unittest
import warnings

from parse_python_indentation import parse_indentation

good_output = [
	{'key': 'green:',
     'offspring': [
		{'key': 'follow', 'offspring': []},
        {'key': 'blue', 'offspring': []},
        {'key': 'yellow', 'offspring': []},
		{'key': 'fishing', 'offspring': []},
		{'key': 'snowman:',
		 'offspring': [
			{'key': 'gardening',
			 'offspring': []
			}
		]},
		{'key': 'street:',
		  'offspring': [{'key': 'great', 'offspring': []}]}]},
		{'key': 'religion', 'offspring': []},
		{'key': 'flags', 'offspring': []},
		{'key': 'houses:',
		 'offspring': [{'key': 'suffering', 'offspring': []}]}
	]


class ParseTests(unittest.TestCase):
	maxDiff = None

	def test_parsing(self):
		""" Tests whether correctly indented file can be parsed
		"""
		with open ("test.data", "r") as input_file:
		    rawdata = input_file.read()
		a = parse_indentation(rawdata)
		self.assertEqual(a,good_output)

	def test_warning(self):
		""" Tests whether file with two extra indentation spaces is parsed and
		creates a warning.
		"""
		with warnings.catch_warnings(record=True) as w:
			with open ("test1.data", "r") as input_file:
				rawdata = input_file.read()
			warnings.simplefilter("always")
			a = parse_indentation(rawdata)
		self.assertEqual(a,good_output)
		self.assertEqual(len(w),1)
		self.assertEqual(str(w[0].message),'Indentation with errors!')


if __name__ == '__main__':
    unittest.main()
