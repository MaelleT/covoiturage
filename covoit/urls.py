'''
Created on 3 août 2016

@author: maelle
'''

from django.conf.urls import url

from . import views
urlpatterns=[
            url(r'$',views.index,name='index')
             ] 