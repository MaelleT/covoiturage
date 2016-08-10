'''
Created on 10 août 2016

@author: maelle
'''
from django import forms

class SearchForm(forms.Form):
    leLieu = forms.CharField(label='Lieu', max_length = 50)