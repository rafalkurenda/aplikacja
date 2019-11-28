from django.db import models


class Pododdzial(models.Model):
    nazwa = models.CharField(max_length=30)


class Oddzialy(models.Model):
    nazwa = models.CharField(max_length=30)
    pododdzial = models.ForeignKey(Pododdzial, on_delete=models.CASCADE)

class Zwiazki_taktyczne(models.Model):
    nazwa = models.CharField(max_length=30)
    oddzialy = models.ForeignKey(Oddzialy, on_delete=models.CASCADE)


class Zwiazki_operacyjne(models.Model):
    nazwa = models.CharField(max_length=30)
    zwiazki_taktyczne = models.ForeignKey(Zwiazki_taktyczne, on_delete=models.CASCADE)

class Adres(models.Model):
    ulica = models.CharField(max_length=30)
    numer = models.CharField(max_length=30)
    kod_pocztowy = models.CharField(max_length=30)
    miejscowosc = models.CharField(max_length=30)

class Stopien(models.Model):
    nazwa = models.CharField(max_length=30)
    wynagrodzenie = models.IntegerField()


class Personel(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    adres = models.ForeignKey(Adres, on_delete=models.CASCADE, related_name="adres_rel")
    stopien = models.OneToOneField(
        Stopien,
        on_delete=models.CASCADE,

    )
    poddodzial = models.OneToOneField(
        Pododdzial,
        on_delete=models.CASCADE,
    )

class Sprzet(models.Model):
    nazwa = models.CharField(max_length=30)
    ilosc = models.IntegerField()


class Baza(models.Model):
    nazwa = models.CharField(max_length=30)
    adres = models.OneToOneField(
        Adres,
        on_delete=models.CASCADE,
    )
    zwiazki_taktyczne = models.ForeignKey(Zwiazki_taktyczne, on_delete=models.CASCADE)
    sprzet = models.ForeignKey(Sprzet, on_delete=models.CASCADE)

