from django.shortcuts import render
from .models import Oddzialy,Zwiazki_taktyczne,Zwiazki_operacyjne,Personel,Pododdzial,Adres,Stopien,Sprzet,Baza
from rest_framework import viewsets, generics
from .serializers import PersonelSer, AdresSer, PododdzialSer, OddzialySer, Zwiazki_operacyjneSer, Zwiazki_taktyczneSer, StopienSer, SprzetSer, BazaSer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PersonelView(viewsets.ModelViewSet):

    queryset = Personel.objects.all()
    serializer_class = PersonelSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdresView(viewsets.ModelViewSet):

    queryset = Adres.objects.all()
    serializer_class = AdresSer

class PododdzialView(viewsets.ModelViewSet):
    queryset = Pododdzial.objects.all()
    serializer_class = PododdzialSer

class OddzialyView(viewsets.ModelViewSet):
    queryset = Oddzialy.objects.all()
    serializer_class = OddzialySer

class Zwiazki_operacyjneView(viewsets.ModelViewSet):
    queryset = Zwiazki_operacyjne.objects.all()
    serializer_class = Zwiazki_operacyjneSer

class Zwiazki_taktyczneView(viewsets.ModelViewSet):
    queryset = Zwiazki_taktyczne.objects.all()
    serializer_class = Zwiazki_taktyczneSer

class StopienView(viewsets.ModelViewSet):
    queryset = Stopien.objects.all()
    serializer_class = StopienSer

class SprzetView(viewsets.ModelViewSet):
    queryset = Sprzet.objects.all()
    serializer_class = SprzetSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(tworca=self.request.user)

class BazaView(viewsets.ModelViewSet):
    queryset = Baza.objects.all()
    serializer_class = BazaSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(tworca=self.request.user)



def index(request):

    return render(request, 'index.html')