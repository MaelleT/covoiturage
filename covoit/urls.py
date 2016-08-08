'''
Created on 3 août 2016

@author: maelle
'''

from django.conf.urls import url

# define namespaces for project with a lot of apps : URL 
app_name = 'covoit'

from . import views
urlpatterns=[
            url(r'^$',views.index,name='index'),
            url(r'^(?P<offreP_id>[0-9]+)/$',views.detailOffreP,name='detailOffreP'),
            url(r'^login/$', 'django.contrib.auth.views.login'),
            url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',{'login_url': '/covoit/login/'}) ] 