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

from main import LandingEcoPage

from sip.sip_description import SIPDescriptionPage
from sip.sip_input import SIPInputPage
from sip.sip_algorithm import SIPAlgorithmPage
from sip.sip_references import SIPReferencesPage
from sip.sip_output import SIPExecutePage

urlpatterns = patterns('',
    # (r'^$', ),
    (r'^eco_index\.html$', LandingEcoPage.as_view()),

    (r'^sip_description\.html$', SIPDescriptionPage.as_view()),
    (r'^sip_input\.html$', SIPInputPage.as_view()),
    (r'^sip_output\.html$', SIPExecutePage.as_view()),
    (r'^sip_algorithms\.html$', SIPAlgorithmPage.as_view()),
    (r'^sip_references\.html$', SIPReferencesPage.as_view()),
    # (r'^sip_history\.html$', genericDescriptionPage.as_view()),
    
    # url(r'^admin/', include(admin.site.urls)),
)