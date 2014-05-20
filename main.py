from django.views.generic import View
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
# from uber import uber_lib

class LandingEcoPage(View):
    def get(self, request):
        text_file1 = open('main_description.txt','r')
        x = text_file1.read()
        text_file2 = open('main_text.txt','r')
        xx = text_file2.read()

        # ChkCookie = self.request.cookies.get("ubercookie")
        # html = uber_lib.SkinChkMain(ChkCookie)
        html = render_to_string('01uberheader_main.html', {})
        html = html + render_to_string('02uberintroblock_nomodellinks.html', {
                'title2':'Ecological Risk Web Applications',
                'title3':x
                })
        html = html + render_to_string('03ubertext_links_left.html', {})                        
        html = html + render_to_string('04ubertext_start_index.html', {
                'text_paragraph':xx
                })
        html = html + render_to_string('04ubertext_end.html',{})
        html = html + render_to_string('05ubertext_links_right.html', {})
        html = html + render_to_string('06uberfooter.html', {'links': ''})

        response = HttpResponse()
        response.write(html)

        return response