from django.views.generic import View
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
# from uber import uber_lib

class SIPDescriptionPage(View):
    def get(self, request):
        text_file2 = open('./sip/sip_text.txt','r')
        xx = text_file2.read()

        # ChkCookie = self.request.cookies.get("ubercookie")
        # html = uber_lib.SkinChk(ChkCookie, "SIP Description")
        html = render_to_string('01uberheader.html', {'title': 'SIP Description'})
        html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':'sip','page':'description'})
        html = html + render_to_string ('03ubertext_links_left.html', {})                
        html = html + render_to_string('04ubertext_start.html', {
			'model_page':'http://www.epa.gov/oppefed1/models/terrestrial/sip/sip_user_guide.html',
			'model_attributes':'SIP Overview',
                 'text_paragraph':xx})
        html = html + render_to_string('04ubertext_end.html', {})
        html = html + render_to_string('05ubertext_links_right.html', {})
        html = html + render_to_string('06uberfooter.html', {'links': ''})
        
        response = HttpResponse()
        response.write(html)

        return response