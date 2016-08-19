from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from covoit.models import OffrePermanente
from django.template import loader
from django.contrib.auth.decorators import login_required
from covoit.forms import SearchForm
from django.db.models.query import QuerySet
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def index(request):
    
    offres_list = OffrePermanente.objects.all()
    context={
             'offres_list':offres_list
             }    
    return render(request,'covoit/index.html',context)

class OffrePermanenteDetailView(DetailView):
    """
    Permet de récupérer l'offrePermanente dont l'id est transmis via le paramètre offreP_id dans l'URL
    Renvoie une erreur 404 en cas d'offre inexistante
    """
    
    model=OffrePermanente
    template_name = 'covoit/detailOffreP.html'
    context_object_name = 'offreP'
    
    def get_object(self):    
        try :
            offreP = OffrePermanente.objects.get(pk=self.kwargs.get("offreP_id"))
        except OffrePermanente.DoesNotExist:
            raise Http404("L'offre n'existe pas")
            
        return offreP

class OffresAut(ListView):

    context_object_name = 'offres_user'
    template_name = 'covoit/mesOffres.html'
    
    def get_queryset(self):
        return OffrePermanente.objects.filter(auteur__username=self.request.user.username)
    
    
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

     

