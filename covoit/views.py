from django.shortcuts import render
from django.http.response import HttpResponse
from covoit.models import OffrePermanente


def index(request):
    offres_list = OffrePermanente.objects.order_by('lieu')
    output = ' | '.join([str(o) for o in offres_list])
    return HttpResponse(output)
