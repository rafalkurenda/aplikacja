from rest_framework import serializers
from .models import Oddzialy,Zwiazki_taktyczne,Zwiazki_operacyjne,Personel,Pododdzial,Adres,Stopien



class PododdzialSer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=30)

class OddzialySer(serializers.Serializer):
    pododdzial = serializers.RelatedField(source='Pododdzial.nazwa', read_only=True)

    class Meta:
        model = Oddzialy
        fields = "__all__"


class Zwiazki_taktyczneSer(serializers.Serializer):

    oddzialy = serializers.RelatedField(source='Oddzialy.nazwa',read_only=True)

    class Meta:
        model = Zwiazki_taktyczne
        fields = "__all__"

class Zwiazki_operacyjneSer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=30)
    zwiazki_taktyczne = serializers.RelatedField(source='Zwiazki_taktyczne.nazwa',read_only=True)

    class Meta:
        model = Zwiazki_taktyczne
        fields = "__all__"

class AdresSer(serializers.Serializer):
    ulica = serializers.CharField(max_length=30)
    numer = serializers.CharField(max_length=30)
    kod_pocztowy = serializers.CharField(max_length=30)
    miejscowosc = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Adres.objects.create(**validated_data)

class StopienSer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=30)
    wynagrodzenie = serializers.IntegerField()

class PersonelSer(serializers.Serializer):
    adres = AdresSer(read_only=True)
    stopien = serializers.CharField(source='Stopien.nazwa')
    poddodzial = serializers.CharField(source='Poddodzial.nazwa')

    class Meta:
        model = Personel
        fields = "__all__"


class SprzetSer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=30)
    ilosc = serializers.IntegerField()

class BazaSer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=30)
    adres = AdresSer(read_only=True)
    zwiazki_taktyczne = serializers.RelatedField(source='Zwiazki_taktyczne.nazwa', read_only=True)
    sprzet = SprzetSer(read_only=True)

