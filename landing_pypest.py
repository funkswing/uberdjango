from django.views.generic import View
from django.template.loader import render_to_string
from django.http import HttpResponse

class UberLandingPage(View):
    def get(self, request):                    
        html = render_to_string('00landing_page.html', {'title':'Ubertool'})

        response = HttpResponse()
        response.write(html)

        return response