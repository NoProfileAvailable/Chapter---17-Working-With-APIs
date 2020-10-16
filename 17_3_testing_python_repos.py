import unittest

from python_repos import status_code
from python_repos import total_repos

class ReposTestCase(unittest.TestCase):
	""" Tests for status_code 200. """

	def test_status_code_200(self):
		"""Tests if the status_code equals 200."""
		formatted_status = status_code(self)
		self.assertEqual(formatted_status, '200')

	def test_repositories(self):
		""" How many repositories came in. """
		tot_repos = total_repos(self)
		#self.assertEqual(tot_repos, "6052353)

if __name__ == '__main__':
	unittest.main()