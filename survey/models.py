# Robin Kalia
# robinkalia@berkeley.edu
# UC Berkeley
#
# models.py: Models defined for the 'Survey' Web App


from django.db import models

import datetime
from django.utils import timezone


class Question(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Published Date')
	
	def __unicode__(self):
		return self.question
		
	def contains_nonempty_text(self):
		return self.question != ''		
		
	def contains_verylong_text(self):
		text_str = self.question	
		return len(text_str) > 200		

	def posted_shortly(self):
		now = timezone.now() 
		return now - datetime.timedelta(days=1) <= self.pub_date <= now 

	posted_shortly.admin_order_field = 'pub_date'
	posted_shortly.boolean = True
	posted_shortly.short_decription = 'Published recently?'


class Choice(models.Model):
	question = models.ForeignKey(Question)	
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.choice_text
		
	def contains_nonempty_text(self):
		return self.choice_text != ''		
		
	def contains_verylong_text(self):
		text_str = self.choice_text		
		return len(text_str) > 200		





