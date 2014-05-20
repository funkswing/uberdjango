from django.views.generic import View
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

import sys
# sys.path.append("../sip")
from sip import sip_model,sip_tables
# from uber import uber_lib
# import rest_funcs

class SIPExecutePage(View):
    def post(self, request):
        chemical_name = request.POST.get('chemical_name')
       # select_receptor = request.POST.get('select_receptor')
       # bw_bird = request.POST.get('body_weight_of_bird')
       # bw_mamm = request.POST.get('body_weight_of_mammal')
        sol = request.POST.get('solubility')
        ld50_a = request.POST.get('ld50_a')
        ld50_m = request.POST.get('ld50_m')
        aw_bird = request.POST.get('aw_bird')
        # tw_bird = request.POST.get('body_weight_of_the_tested_bird')
        aw_mamm = request.POST.get('aw_mamm')
        # tw_mamm = request.POST.get('body_weight_of_the_tested_mammal')
        mineau = request.POST.get('mineau_scaling_factor')
        noael = request.POST.get('NOAEL')
        noaec_d = request.POST.get('NOAEC_d')
        noaec_q = request.POST.get('NOAEC_q')
        noaec_o = request.POST.get('NOAEC_o')
        # noaec_o2 = request.POST.get('NOAEC_o2')
        Species_of_the_bird_NOAEC_CHOICES = request.POST.get('NOAEC_species')
        bw_quail = request.POST.get('bw_quail')
        bw_duck = request.POST.get('bw_duck')
        bwb_other = request.POST.get('bwb_other')
        bw_rat = request.POST.get('bw_rat')
        bwm_other = request.POST.get('bwm_other')
        b_species = request.POST.get('b_species')
        m_species = request.POST.get('m_species')
        print 'aw_bird = %s'%aw_bird
        sip_obj = sip_model.sip(True,True,'single',chemical_name, b_species, m_species, bw_quail, bw_duck, bwb_other, bw_rat, bwm_other, sol, ld50_a, ld50_m, aw_bird, mineau, aw_mamm, noaec_d, noaec_q, noaec_o, Species_of_the_bird_NOAEC_CHOICES, noael)
        

        # ChkCookie = self.request.cookies.get("ubercookie")
        # html = uber_lib.SkinChk(ChkCookie, "SIP Output")
        html = render_to_string('01uberheader.html', {'title': 'SIP Output'})
        html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':'sip','page':'output'})
        html = html + render_to_string('03ubertext_links_left.html', {})                
        html = html + render_to_string('04uberoutput_start.html', {
                'model':'sip', 
                'model_attributes':'SIP Output'})
        # html = html + sip_tables.timestamp(sip_obj)
        html = html + sip_tables.table_all(sip_obj)
        # html = html + render_to_string('export.html', {})
        html = html + render_to_string('04uberoutput_end.html', {})
        html = html + render_to_string('06uberfooter.html', {'links': ''})
        # rest_funcs.save_dic(html, sip_obj.__dict__, "sip", "single")
        
        response = HttpResponse()
        response.write(html)

        return response