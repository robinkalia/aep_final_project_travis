# Robin Kalia
# robinkalia@berkeley.edu
# UC Berkeley
#
# Urls.py: Urls used in the 'Survey' Web Application


from django.conf.urls import url

from survey import views

urlpatterns = [
	# Manual Views
	# url(r'^$', views.index, name='index'),
	# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# Generic Views
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

