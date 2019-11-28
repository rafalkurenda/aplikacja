from rest_framework import serializers
from .models import Oddzialy,Zwiazki_taktyczne,Zwiazki_operacyjne,Personel,Pododdzial,Adres,Stopien,Sprzet,Baza



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

    class Meta:
        model = Personel
        fields = "__all__"


class SprzetSer(serializers.ModelSerializer):
    class Meta:
        model = Sprzet
        fields = "__all__"

class BazaSer(serializers.ModelSerializer):
    class Meta:
        model = Baza
        fields = "__all__"

