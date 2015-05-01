# Robin Kalia
# robinkalia@berkeley.edu
# UC Berkeley
#
# Views.py: Views that are mapped by the 'URLs' used in the 'Survey' Web Application


from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

from django.utils import timezone
from django.views import generic

from survey.models import Question, Choice


def index(request):
	""" index(): Manual Index View """
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('survey/index.html')
	context = RequestContext(request, { 'latest_question_list' : latest_question_list})
	context2 = { 'latest_question_list' : latest_question_list }	
	list_response = '\n'.join([p.question for p in latest_question_list])
	response_init = "This is a simple Web App for Survey: \n\n"
	response = response_init + list_response
	# return HttpResponse(response)
	# return HttpResponse(template.render(context))
	return render(request, 'survey/index.html', context2)

class IndexView(generic.ListView):
	""" IndexView(): Generic Index View """
	template_name = 'survey/index.html'
	context_object_name = 'latest_question_list'	
	
	def get_queryset(self):
		#return Question.objects.order_by('-pub_date')[:5]
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


def detail(request, question_id):
	""" detail(): Manual Detail View """
	"""
	try:
		q = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404
	"""
	q = get_object_or_404(Question, pk=question_id)
	context = { 'question' : q }
	return render(request, 'survey/detail.html', context)

class DetailView(generic.DetailView):
	"""" DetailView(): Generic Detail View """
	model = Question
	template_name = 'survey/detail.html'


def vote(request, question_id):
	q = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = q.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		context = { 'question' : q, 'error_message' : "You didn't select a choice" } 
		return render(request, 'survey/detail.html', context)

	selected_choice.votes += 1
	selected_choice.save()
	return HttpResponseRedirect(reverse('survey:results', args=(q.id,)))


def results(request, question_id):
	q = get_object_or_404(Question, pk=question_id)
	context = {'question' : q}
	return render(request, 'survey/results.html', context)

class ResultsView(generic.DetailView):
	"""" DetailView(): Generic Results View """
	model = Question
	template_name = 'survey/results.html'


