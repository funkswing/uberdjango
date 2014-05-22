$(document).ready(function() {
  $('#id_bw_quail').closest('tr').hide();
  $('#id_bw_duck').closest('tr').hide();
  $('#id_bwb_other').closest('tr').hide();
  $('#id_bw_rat').closest('tr').hide();
  $('#id_bwm_other').closest('tr').hide();
  $('#id_NOAEC_d').closest('tr').hide();
  $('#id_NOAEC_q').closest('tr').hide();
  $('#id_NOAEC_o').closest('tr').hide();

  $('#id_b_species').change(function() { 
      if ($(this).val() == "178"){
          $('#id_bw_quail').closest('tr').show();
          $('#id_bw_duck').closest('tr').hide();
          $('#id_bwb_other').closest('tr').hide();
      }
      else if ($(this).val() == "1580"){
          $('#id_bw_duck').closest('tr').show();
          $('#id_bw_quail').closest('tr').hide();
          $('#id_bwb_other').closest('tr').hide();
      }
      else{
         $('#id_bwb_other').closest('tr').show();
         $('#id_bw_duck').closest('tr').hide();
         $('#id_bw_quail').closest('tr').hide();
     }
     if ($(this).val() == "0"){
         $('#id_bwb_other').closest('tr').hide();
         $('#id_bw_duck').closest('tr').hide();
         $('#id_bw_quail').closest('tr').hide();
     }
   });
  $('#id_m_species').change(function() {
      if ($(this).val() == "350"){
          $('#id_bw_rat').closest('tr').show();
          $('#id_bwm_other').closest('tr').hide();
      }
      else{
         $('#id_bw_rat').closest('tr').hide();
         $('#id_bwm_other').closest('tr').show();
      }
      if ($(this).val() == "0"){
          $('#id_bw_rat').closest('tr').hide();
          $('#id_bwm_other').closest('tr').hide();
      }
  });
  $('#id_NOAEC_species').change(function() {
      if ($(this).val() == "1"){
          $('#id_NOAEC_q').closest('tr').show();
          $('#id_NOAEC_d').closest('tr').hide();
          $('#id_NOAEC_o').closest('tr').hide();
      }
      else if ($(this).val() == "2"){
          $('#id_NOAEC_d').closest('tr').show();
          $('#id_NOAEC_q').closest('tr').hide();
          $('#id_NOAEC_o').closest('tr').hide();
      }
      else{
         $('#id_NOAEC_o').closest('tr').show();
         $('#id_NOAEC_d').closest('tr').hide();
         $('#id_NOAEC_q').closest('tr').hide();
     }
     if ($(this).val() == "0"){
         $('#id_NOAEC_d').closest('tr').hide();
         $('#id_NOAEC_q').closest('tr').hide();
         $('#id_NOAEC_o').closest('tr').hide();
     }
   });
});