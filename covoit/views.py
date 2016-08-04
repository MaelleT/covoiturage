from django.shortcuts import render
from django.http.response import HttpResponse
from covoit.models import OffrePermanente
from django.template import loader


def index(request):
    
    offres_list = OffrePermanente.objects.order_by('lieu')
    context={
             'offres_list':offres_list
             }    
    return render(request,'covoit/index.html',context)

def detailOffreP(request,offreP_id):
    """
    Renvoie les informations concernant l'offre permanente dont l'id est transmis via l'url
    """
    offreP = OffrePermanente.objects.get(pk=offreP_id)
    
    return render(request,'covoit/detailOffreP.html',{'offreP':offreP})
    
    