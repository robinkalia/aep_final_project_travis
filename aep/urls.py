# Robin Kalia
# robinkalia@berkeley.edu
# UC Berkeley
#
# Urls.py: Root Url that includes the various urls of all apps in the main project - 'aep'

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^aep/survey/', include('survey.urls', namespace='survey')),
    url(r'^aep/admin/', include(admin.site.urls)),
]
