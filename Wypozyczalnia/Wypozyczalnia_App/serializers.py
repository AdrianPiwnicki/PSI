from .models import Klient, Samochod, Pracownik, Wypozyczanie
from rest_framework import serializers

class KlientSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    PESEL = serializers.IntegerField(required=True)
    Imie = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Nazwisko = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Numer_Prawa_Jazdy = serializers.CharField(required=True, max_length=13)

    def create(self, validated_data):
        return Klient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Imie = validated_data.get('Imie', instance.Imie)
        instance.Nazwisko = validated_data.get('Nazwisko', instance.Nazwisko)
        instance.Numer_Prawa_Jazdy = validated_data.get('Numer_Prawa_Jazdy', instance.Numer_Prawa_Jazdy)
        instance.save()
        return instance


class SamochodSerializer(serializers.Serializer):
    VIN = serializers.IntegerField(required=True)
    Marka = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Model = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Dostepnosc = serializers.IntegerField(required=False)
    CenaZaDobe = serializers.FloatField(required=False)

    def create(self, validated_data):
        return Samochod.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Marka = validated_data.get('Marka', instance.Marka)
        instance.Model = validated_data.get('Model', instance.Model)
        instance.Dostepnosc = validated_data.get('Dostepnosc', instance.Dostepnosc)
        instance.CenaZaDobe = validated_data.get('CenaZaDobe', instance.CenaZaDobe)
        instance.save()
        return instance


class PracownikSerializer(serializers.Serializer):
    idPracownik = serializers.IntegerField(required=True)
    Imie = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Nazwisko = serializers.CharField(required=False, allow_blank=True, max_length=45)
    Stanowisko = serializers.CharField(required=False, allow_blank=True, max_length=45)

    def create(self, validated_data):
        return Pracownik.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idPracownik = validated_data.get('idPracownik', instance.idPracownik)
        instance.Imie = validated_data.get('Imie', instance.Imie)
        instance.Nazwisko = validated_data.get('Nazwisko', instance.Nazwisko)
        instance.Stanowisko = validated_data.get('Stanowisko', instance.Stanowisko)
        instance.save()
        return instance


class WypozyczanieSerializer(serializers.Serializer):
    idWypozyczanie = serializers.IntegerField(required=True)
    Klient_PESEL = serializers.PrimaryKeyRelatedField(queryset=Klient.objects.all())
    Samochod_VIN = serializers.PrimaryKeyRelatedField(queryset=Samochod.objects.all())
    Pracownik_idPracownika = serializers.PrimaryKeyRelatedField(queryset=Pracownik.objects.all())
    Data_rozpoczecia = serializers.DateField(required=False)
    Data_zakonczenia = serializers.DateField(required=False)
    Cena_za_wypozyczenie = serializers.FloatField(required=False)

    def create(self, validated_data):
        return Wypozyczanie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idWypozyczanie = validated_data.get('idWypozyczanie', instance.idWypozyczanie)
        instance.Data_rozpoczecia = validated_data.get('Data_rozpoczecia', instance.Data_rozpoczecia)
        instance.Data_zakonczenia = validated_data.get('Data_zakonczenia', instance.Data_zakonczenia)
        instance.Cena_za_wypozyczenie = validated_data.get('Cena_za_wypozyczenie', instance.Cena_za_wypozyczenie)
        instance.save()
        return instance