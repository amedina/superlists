#!/usr/bin/env python3

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicity_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool To-Do App and she goes to the website
		# to check it out
		self.browser.get('http://127.0.0.1:8000')

		# She notices the page title and header mention to-do lists

		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# She is invited to enter a to-do right away

		# She enters "Buy peacock feathers into a text box

		# When she hits enter the page updates, and now the page lists
		# "1. Buy peacock feathers" as an item in a to-do list
    
		# There is still a text box inviting her to add another to-do
		# She enters "Use peacock feathers to make a fly"
    
		# The page updates again, and now it shows both items
		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.

		# She visits that URL - her to-do list is still there.


if __name__ == "__main__":
	unittest.main(warnings='ignore')
