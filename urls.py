# from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# )


#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# from polls.views import Index
from generic.generic_description import genericDescriptionPage
from sip.sip_description import SIPDescriptionPage
from sip.sip_input import SIPInputPage
from sip.sip_algorithm import SIPAlgorithmPage
from sip.sip_references import SIPReferencesPage
from sip.sip_output import SIPExecutePage

urlpatterns = patterns('',
    # url(r'^polls/', include('polls.urls')),
    # (r'^polls/latest\.html$', 'polls.views.index'),
    # (r'^polls\.html/$', 'polls.views.index'),
    # (r'^polls\.html/$', Index.as_view()),
    (r'^generic_description\.html$', genericDescriptionPage.as_view()),
    (r'^sip_description\.html$', SIPDescriptionPage.as_view()),
    (r'^sip_input\.html$', SIPInputPage.as_view()),
    (r'^sip_output\.html$', SIPExecutePage.as_view()),
    (r'^sip_algorithms\.html$', SIPAlgorithmPage.as_view()),
    (r'^sip_references\.html$', SIPReferencesPage.as_view()),
    # (r'^sip_history\.html$', genericDescriptionPage.as_view()),
    # url(r'^admin/', include(admin.site.urls)),
)