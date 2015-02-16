#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool To-Do App and she goes to the website
		# to check it out
		self.browser.get('http://127.0.0.1:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do right away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# She enters "Buy peacock feathers into a text box
		inputbox.send_keys('Buy peacock feathers')

		# When she hits enter the page updates, and now the page lists
		# "1. Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		# self.assertTrue(
		# 	any(row.text == '1: Buy peacock feathers' for row in rows),
		# 		"New to-do item does not appear on list -- its text was:\n%s" % (
		# 			table.text)
		# )

		# There is still a text box inviting her to add another to-do
		# She enters "Use peacock feathers to make a fly"
		self.fail('Finish the test!')

		# The page updates again, and now it shows both items
		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.

		# She visits that URL - her to-do list is still there.


if __name__ == "__main__":
	unittest.main(warnings='ignore')
