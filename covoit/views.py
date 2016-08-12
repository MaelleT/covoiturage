from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from covoit.models import OffrePermanente
from django.template import loader
from django.contrib.auth.decorators import login_required
from covoit.forms import SearchForm
from django.db.models.query import QuerySet
from django.core.urlresolvers import reverse


def index(request):
    
    offres_list = OffrePermanente.objects.all()
    context={
             'offres_list':offres_list
             }    
    return render(request,'covoit/index.html',context)

def detailOffreP(request,offreP_id):
    """
    Renvoie les informations concernant l'offre permanente dont l'id est transmis via l'url. Génére une erreur 404 si l'id ne correspond à aucune offre
    """
    try :
        offreP = OffrePermanente.objects.get(pk=offreP_id)
    except OffrePermanente.DoesNotExist:
        raise Http404("L'offre n'existe pas")
    
    return render(request,'covoit/detailOffreP.html',{'offreP':offreP})

@login_required
def mesOffres(request): 
    offres_user = OffrePermanente.objects.filter(auteur__username=request.user.username)
    context={
             'offres_user':offres_user
             }
    return render(request,'covoit/mesOffres.html',context)


def rechercherForm(request):
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            offres = OffrePermanente.objects.filter(lieu__libelle = form.cleaned_data['leLieu'])
            return render(request,'covoit/lesOffresRecherchees.html',{'offres':offres})

        else :
            return render(request,'covoit/rechercherForm.html',{'form':form})

    else :
        form= SearchForm()
        return render(request,'covoit/rechercherForm.html',{'form':form})

     

