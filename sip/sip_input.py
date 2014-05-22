from django.views.generic import View
# from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from sip import sip_parameters,sip_tooltips
# from uber import uber_lib

class SIPInputPage(View):
    def get(self, request):
        text_file = open('./sip/sip_description.txt','r')
        x = text_file.read()
        
        # ChkCookie = self.request.cookies.get("ubercookie")
        # html = uber_lib.SkinChk(ChkCookie, "SIP Inputs")
        html = render_to_string('01uberheader.html', {'title': 'SIP Inputs'})
        html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':'sip','page':'input'})
        html = html + render_to_string('03ubertext_links_left.html', {}) 
        html = html + render_to_string('sip-jquery.html', {})               
        html = html + render_to_string('04uberinput_start.html', {
                'model':'sip', 
                'model_attributes':'SIP Inputs'})
        html = html + render_to_string('sip_ubertool_config_input.html', {})  
        html = html + str(sip_parameters.SIPInp())
        html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
        html = html + render_to_string('sip_ubertool_config.html', {})
        # Check if tooltips dictionary exists
        if hasattr(sip_tooltips, 'tooltips'):
            tooltips = sip_tooltips.tooltips
        else:
            tooltips = {}
        html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})
        html = html + render_to_string('06uberfooter.html', {'links': ''})

        response = HttpResponse()
        response.write(html)

        return response