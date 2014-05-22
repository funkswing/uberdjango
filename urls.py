#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', 'views.ubertoolLandingPage'),
    (r'^eco/?$', 'views.ecoLandingPage'),
    (r'^eco/(?P<model>.*?)/description/?$', 'views.descriptionPage'),
    (r'^eco/(?P<model>.*?)/input/?$', 'views.inputPage'),
    (r'^eco/(?P<model>.*?)/output/?$', 'views.outputPage'),
    (r'^eco/(?P<model>.*?)/algorithms/?$', 'views.algorithmPage'),
    (r'^eco/(?P<model>.*?)/references/?$', 'views.referencesPage'),
    # (r'^eco/(?P<model>.*?)/history/?$', 'views.historyPage'),
    (r'^eco/(?P<model>.*?)/?$', 'views.descriptionPage'),
    (r'^eco_index\.html$', 'views.ecoLandingPage'),                     #Legacy links
    (r'^(?P<model>.*?)_description\.html$', 'views.descriptionPage'),   #Legacy links
    (r'^(?P<model>.*?)_input\.html$', 'views.inputPage'),               #Legacy links
    (r'^(?P<model>.*?)_output\.html$', 'views.outputPage'),             #Legacy links
    (r'^(?P<model>.*?)_algorithms\.html$', 'views.algorithmPage'),      #Legacy links
    (r'^(?P<model>.*?)_references\.html$', 'views.referencesPage'),     #Legacy links
    # (r'^(?P<model>.*?)_history\.html$', 'views.historyPage',          #Legacy links
    # url(r'^admin/', include(admin.site.urls)),
)

# 404 Error view (file not found)
handler404 = 'views.fileNotFound'
# 500 Error view (server error)
handler500 = 'views.fileNotFound'
# 403 Error view (forbidden)
handler403 = 'views.fileNotFound'