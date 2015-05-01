# Robin Kalia
# robinkalia@berkeley.edu
# UC Berkeley
#
# admin.py: Admin utilities defined for the 'Survey' Web App


from django.contrib import admin
from survey.models import Question, Choice


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question']}),
		('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
	]

	inlines = [ChoiceInline]

	list_display = ('question', 'pub_date', 'posted_shortly')
 	list_filter = ['question', 'pub_date']
	search_fields = ['question']		


admin.site.register(Question, QuestionAdmin)

