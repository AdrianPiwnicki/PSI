from django.db import models


class Klient(models.Model):
    PESEL = models.IntegerField(primary_key=True)
    Imię = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Numer_Prawa_Jazdy = models.CharField(max_length=13)
    def __str__(self):
        return '%s %s %s %s' %(self.PESEL, self.Imię, self.Nazwisko, self.Numer_Prawa_Jazdy)


class Samochód(models.Model):
    VIN = models.CharField(primary_key=True, max_length=100)
    Marka = models.CharField(max_length=45)
    Model = models.CharField(max_length=45)
    Dostępność = models.IntegerField()
    CenaZaDobę = models.FloatField()
    def __str__(self):
        return '%s %s %s %s %s' % (self.VIN, self.Marka, self.Model, self.Dostępność, self.CenaZaDobę)


class Pracownik(models.Model):
    idPracownik = models.IntegerField(primary_key=True)
    Imię = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Stanowisko = models.CharField(max_length=45)
    def __str__(self):
        return '%s %s %s %s' % (self.idPracownik, self.Imię, self.Nazwisko, self.Stanowisko)


class Wypożyczanie(models.Model):
    idWypożyczanie = models.IntegerField(primary_key=True)
    Klient_PESEL = models.ForeignKey(Klient, on_delete=models.CASCADE)
    Samochód_VIN = models.ForeignKey(Samochód, on_delete=models.CASCADE)
    Pracownik_idPracownika = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    Data_rozpoczęcia = models.DateField()
    Data_zakończenia = models.DateField()
    Cena_za_wypożyczenie = models.FloatField()
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.idWypożyczanie, self.Klient_PESEL, self.Samochód_VIN, self.Pracownik_idPracownika, self.Data_rozpoczęcia,
                                   self.Data_zakończenia, self.Cena_za_wypożyczenie)
