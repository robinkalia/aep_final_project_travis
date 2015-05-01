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


class QuestionMethodsTest(TestCase):

	def test_contains_nonempty_text_with_empty_text(self):
		question = Question(question = '')
		self.assertFalse(question.contains_nonempty_text())			
	def test_contains_nonempty_text_with_valid_text(self):
		question = Question(question = 'Who will win the 2016 Presidential election?')
		self.assertTrue(question.contains_nonempty_text())
  
	def test_contains_verylong_text_with_normal_size_text(self):
		question = Question(question = 'Who will win the 2016 SuperBowl championship?')
		self.assertFalse(question.contains_verylong_text())
 
	def test_contains_verylong_text_with_big_size_text(self):
		text_str = "Who will win the 2016 SuperBowl championship?"
		question = Question(question = "{:201}".format(text_str))
		self.assertTrue(question.contains_verylong_text())

	def test_posted_shortly_with_future_question(self):
		now = timezone.now() + datetime.timedelta(days=22)
		future_question = Question(pub_date = now)
		self.assertFalse(future_question.posted_shortly())

	def test_posted_shortly_with_old_question(self):
		now = timezone.now() - datetime.timedelta(days=22)
		old_question1 = Question('Who will win the 2016 Presidential election?', pub_date = now)
		self.assertFalse(old_question1.posted_shortly())

	def test_posted_shortly_with_recent_question(self):
		now = timezone.now() - datetime.timedelta(hours=4)
		recent_question = Question('Who will win the 2016 SuperBowl championship?', pub_date = now)
		self.assertTrue(recent_question.posted_shortly())


def create_question(question_text, num_of_days):
	time = timezone.now() + datetime.timedelta(days = num_of_days)
	return Question.objects.create(question = question_text, pub_date = time)

# Functional Tests
class QuestionViewsTest(TestCase):

	def test_index_view_with_no_questions(self):
		response = self.client.get(reverse('survey:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No Survey questions are available as of now.")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])
		
	def test_index_view_with_an_old_question(self):
		create_question(question_text='Who will win the 2016 SuperBowl championship?', num_of_days = -22)
		response = self.client.get(reverse('survey:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Who will win the 2016 SuperBowl championship?>'])

	def test_index_view_with_a_future_question(self):
		create_question(question_text='Who will win WWE SummerSlam 2016?', num_of_days=22)
		response = self.client.get(reverse('survey:index'))
		self.assertContains(response, "No Survey questions are available as of now.", status_code=200)
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_index_view_with_old_and_future_questions(self):
		create_question(question_text="Who is the greatest WWE SuperStar of all time?", num_of_days=-22)
		create_question(question_text="Who is the greatest WWE Championship holder of the past 3 decades?", num_of_days=22)
		response = self.client.get(reverse('survey:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Who is the greatest WWE SuperStar of all time?>'])

	def test_index_view_with_two_old_questions(self):
		create_question(question_text="Who is the greatest WWE SuperStar of all time?", num_of_days=-22)
		create_question(question_text="Who is the greatest WWE Championship holder of the past 3 decades?", num_of_days=-5)
		response = self.client.get(reverse('survey:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Who is the greatest WWE Championship holder of the past 3 decades?>', '<Question: Who is the greatest WWE SuperStar of all time?>'])








