from django.db import models


class Klient(models.Model):
    PESEL = models.IntegerField(primary_key=True)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Numer_Prawa_Jazdy = models.CharField(max_length=13)
    def __str__(self):
        return '%s %s %s %s' %(self.PESEL, self.Imie, self.Nazwisko, self.Numer_Prawa_Jazdy)


class Samochod(models.Model):
    VIN = models.CharField(primary_key=True, max_length=100)
    Marka = models.CharField(max_length=45)
    Model = models.CharField(max_length=45)
    Dostepnosc = models.IntegerField()
    CenaZaDobe = models.FloatField()
    def __str__(self):
        return '%s %s %s %s %s' % (self.VIN, self.Marka, self.Model, self.Dostepnosc, self.CenaZaDobe)


class Pracownik(models.Model):
    idPracownik = models.IntegerField(primary_key=True)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Stanowisko = models.CharField(max_length=45)
    def __str__(self):
        return '%s %s %s %s' % (self.idPracownik, self.Imie, self.Nazwisko, self.Stanowisko)


class Wypozyczanie(models.Model):
    idWypozyczanie = models.IntegerField(primary_key=True)
    Klient_PESEL = models.ForeignKey(Klient, on_delete=models.CASCADE)
    Samochod_VIN = models.ForeignKey(Samochod, on_delete=models.CASCADE)
    Pracownik_idPracownika = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    Data_rozpoczecia = models.DateField()
    Data_zakonczenia = models.DateField()
    Cena_za_wypozyczenie = models.FloatField()
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.idWypozyczanie, self.Klient_PESEL, self.Samochod_VIN, self.Pracownik_idPracownika, self.Data_rozpoczecia,
                                   self.Data_zakonczenia, self.Cena_za_wypozyczenie)
