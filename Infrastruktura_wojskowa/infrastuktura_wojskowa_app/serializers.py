from rest_framework import serializers

class Personel(serializers.Serializer):

class PododdzialSer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=30)

class OddzialySer(serializers.Serializer):
    pododdzial = PododdzialSer(many=False, read_only=True)

    class Meta:
        model = Oddzialy



class Zwiazki_taktyczneSer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=30)
    oddzialy = serializers.RelatedField(source='Oddzialy',read_only=True)
class Zwiazki_operacyjneSer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=30)
    zwiazki_taktyczne = serializers.RelatedField(source='Zwiazki Taktyczne',read_only=True)

class AdresSer(serializers.Serializer):
    ulica = serializers.CharField(max_length=30)
    numer = serializers.CharField(max_length=30)
    kod_pocztowy = serializers.CharField(max_length=30)
    miejscowosc = serializers.CharField(max_length=30)

class StopienSer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=30)
    wynagrodzenie = serializers.IntegerField()

class PersonelSer(serializers.Serializer):
    imie = serializers.CharField(max_length=30)
    nazwisko = serializers.CharField(max_length=30)
    stopien = serializers.IntegerField()
    adres = serializers.ForeignKey(Adres, on_delete=models.CASCADE)
    stopien = serializers.OneToOneField(
        Stopien,
        on_delete=models.CASCADE,

    )
    poddodzial = models.OneToOneField(
        Pododdzial,
        on_delete=models.CASCADE,
    )

class SprzetSer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=30)
    ilosc = serializers.IntegerField()

class BazaSer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=30)
    adres = serializers.OneToOneField(
        Adres,
        on_delete=models.CASCADE,
    )
    zwiazki_taktyczne = serializers.RelatedField(Zwiazki_taktyczne, on_delete=models.CASCADE)
    sprzet = serializers.RelatedField(Sprzet, on_delete=models.CASCADE)

