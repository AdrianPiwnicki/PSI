from django.db import models

class Samochód(models.Model):
    VIN = models.IntegerField()
    Marka = models.CharField(max_length=45)
    Model = models.CharField(max_length=45)
    Dostępność = models.IntegerField()
    Cena_za_dobę = models.FloatField()

class Klient(models.Model):
    PESEL = models.IntegerField(max_length=11)
    Imię = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Numer_prawo_jazdy = models.CharField(max_length=13)

class Pracownik(models.Model):
    idPracownik = models.IntegerField()
    Imię = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Stanowisko = models.CharField(max_length=45)

class Wypożyczenie(models.Model):
    idWypożyczenia = models.IntegerField()
    Klient_PESEL = models.ForeignKey(Klient.PESEL, on_delete=models.CASCADE)
    Samochód_VIN = models.ForeignKey(Samochód.VIN, on_delete=models.CASCADE)
    Pracownik_idPracownik = models.ForeignKey(Pracownik.idPracownik, on_delete=models.CASCADE)
    Data_rozpoczęcia = models.DateTimeField()
    Data_zakończenia = models.DateTimeField()
    Cena_za_wypożyczenie = models.FloatField()