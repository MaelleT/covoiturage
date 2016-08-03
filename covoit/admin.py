from django.contrib import admin
from covoit.models import TypeOffre, Lieu, Jour, OffrePermanente

# Register your models here.
admin.site.register(TypeOffre)
admin.site.register(Lieu)
admin.site.register(Jour)
admin.site.register(OffrePermanente)