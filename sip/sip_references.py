from django.views.generic import View
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
# from uber import uber_lib

class SIPReferencesPage(View):
    def get(self, request):
        text_file1 = open('./sip/sip_references.txt','r')
        x = text_file1.read()
        
        # ChkCookie = self.request.cookies.get("ubercookie")
        # html = uber_lib.SkinChk(ChkCookie, "SIP References")
        html = render_to_string('01uberheader.html', {'title': 'SIP References'})
        html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':'sip','page':'references'})
        html = html + render_to_string('03ubertext_links_left.html', {})
        html = html + render_to_string('04uberreferences_start.html', {
                'model':'sip', 
                'model_attributes':'SIP References', 
                'text_paragraph':x})
        html = html + render_to_string('04ubertext_end.html', {})
        html = html + render_to_string('05ubertext_links_right.html', {})
        html = html + render_to_string('06uberfooter.html', {'links': ''})
        
        response = HttpResponse()
        response.write(html)

        return response