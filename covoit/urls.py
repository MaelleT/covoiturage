'''
Created on 3 août 2016

@author: maelle
'''

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
# define namespaces for project with a lot of apps : URL 
app_name = 'covoit'

from . import views
urlpatterns=[
            url(r'^$',views.index,name='index'),
            #ex : /covoit/offrePermanente/3/
            url(r'^offrePermanente/(?P<offreP_id>[0-9]+)/$',views.OffrePermanenteDetailView.as_view(),name='detailOffreP'),
            url(r'^login/$', auth_views.login,name='login'),
            url(r'^logout/$',auth_views.logout_then_login,{'login_url': '/covoit/login/'},name='logout'),
            url(r'^mesOffres/$', login_required(views.OffresAut.as_view())),
            url(r'^rechercher/$',views.rechercherForm,name='rechercherForm')
            ] 