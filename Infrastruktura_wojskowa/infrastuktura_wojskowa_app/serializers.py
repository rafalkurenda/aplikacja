from rest_framework import serializers
from .models import Oddzialy,Zwiazki_taktyczne,Zwiazki_operacyjne,Personel,Pododdzial,Adres,Stopien,Sprzet,Baza
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        tworcasprzet = serializers.PrimaryKeyRelatedField(many=True, queryset=Sprzet.objects.all())
        tworcabaza = serializers.PrimaryKeyRelatedField(many=True, queryset=Baza.objects.all())
        model = User
        fields = ['id','username', 'tworcasprzet','tworcabaza']

class PododdzialSer(serializers.ModelSerializer):

    class Meta:
        model = Pododdzial
        fields = "__all__"

class OddzialySer(serializers.ModelSerializer):

    class Meta:
        model = Oddzialy
        fields = "__all__"


class Zwiazki_taktyczneSer(serializers.ModelSerializer):

    class Meta:
        model = Zwiazki_taktyczne
        fields = "__all__"

class Zwiazki_operacyjneSer(serializers.ModelSerializer):

    class Meta:
        model = Zwiazki_operacyjne
        fields = "__all__"

class AdresSer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = "__all__"


class StopienSer(serializers.ModelSerializer):
    class Meta:
        model = Stopien
        fields = "__all__"


class PersonelSer(serializers.ModelSerializer):
    adres = serializers.CharField(source="adres.ulica", read_only=True)
    numer = serializers.CharField(source="adres.numer", read_only=True)
    stopien = serializers.CharField(source="stopien.nazwa", read_only=True)
    pododdzial = serializers.CharField(source="pododdzial.nazwa", read_only=True)
    class Meta:

        model = Personel
        fields = "__all__"

class SprzetSer(serializers.ModelSerializer):
    class Meta:
        tworca = serializers.ReadOnlyField(source='tworcasprzet.username')
        model = Sprzet
        fields = "__all__"

class BazaSer(serializers.ModelSerializer):
    class Meta:
        tworca = serializers.ReadOnlyField(source='tworcabaza.username')
        model = Baza
        fields = "__all__"



