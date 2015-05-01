# Robin Kalia
# robinkalia@berkeley.edu
# UC Berkeley
#
# tests.py: Various Tests for individual Views that are utilized in the 'Survey' Web Application

import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from models import Question, Choice

# Unit Tests
class ChoiceMethodsTest(TestCase):

	def test_contains_nonempty_text_with_empty_text(self):
		choice = Choice(choice_text = '')
		self.assertFalse(choice.contains_nonempty_text())			 
	def test_contains_nonempty_text_with_valid_text(self):
		choice = Choice(choice_text = 'San Francisco 49ers')
		self.assertTrue(choice.contains_nonempty_text())
 
	def test_contains_verylong_text_with_normal_size_text(self):
		choice = Choice(choice_text = 'Tarantula')
		self.assertFalse(choice.contains_verylong_text())
 
	def test_contains_verylong_text_with_big_size_text(self):
		text_str = "London"
		choice = Choice(choice_text =  "{:201}".format(text_str))
		self.assertTrue(choice.contains_verylong_text())



