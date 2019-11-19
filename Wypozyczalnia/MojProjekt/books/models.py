from django.db import models


class Klient(models.Model):
    PESEL = models.IntegerField(primary_key=True)
    Imię = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Numer_Prawa_Jazdy = models.CharField(max_length=13)

class Samochód(models.Model):
    VIN = models.CharField(primary_key=True, max_length=100)
    Marka = models.CharField(max_length=45)
    Model = models.CharField(max_length=45)
    Dostępność = models.IntegerField()
    CenaZaDobę = models.FloatField()

class Pracownik(models.Model):
    idPracownik = models.IntegerField(primary_key=True)
    Imię = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Stanowisko = models.CharField(max_length=45)

class Wypożyczanie(models.Model):
    idWypożyczanie = models.IntegerField(primary_key=True)
    Klient_PESEL = models.ForeignKey(Klient, on_delete=models.CASCADE)
    Samochód_VIN = models.ForeignKey(Samochód, on_delete=models.CASCADE)
    Pracownik_idPracownika = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    Data_rozpoczęcia = models.DateField()
    Data_zakończenia = models.DateField()
    Cena_za_wypożyczenie = models.FloatField()