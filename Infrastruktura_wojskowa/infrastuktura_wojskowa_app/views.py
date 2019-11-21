from django.shortcuts import render
from .models import Personel, Adres
from rest_framework import viewsets
from .serializers import PersonelSer, AdresSer


class PersonelView(viewsets.ModelViewSet):

    queryset = Personel.objects.all()
    serializer_class = PersonelSer


class AdresView(viewsets.ModelViewSet):

    queryset = Adres.objects.all()
    serializer_class = AdresSer



def index(request):

    return render(request, 'index.html')