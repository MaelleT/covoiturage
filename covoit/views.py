from django.shortcuts import render
from django.http.response import HttpResponse
from covoit.models import OffrePermanente
from django.template import loader


def index(request):
    
    offres_list = OffrePermanente.objects.order_by('lieu')
    
    template = loader.get_template('covoit/index.html')
    context={
             'offres_list':offres_list
             }    
    return HttpResponse(template.render(context,request))
    