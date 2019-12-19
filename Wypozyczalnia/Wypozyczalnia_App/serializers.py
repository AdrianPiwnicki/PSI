from .models import Klient, Samochod, Pracownik, Wypozyczanie
from rest_framework import serializers


class KlientSerializer(serializers.Serializer):
    class Meta:
        model = Klient
        fields = '__all__'


class SamochodSerializer(serializers.Serializer):
    class Meta:
        model = Samochod
        fields = '__all__'


class PracownikSerializer(serializers.Serializer):
    class Meta:
        model = Pracownik
        fields = '__all__'


class WypozyczanieSerializer(serializers.Serializer):
    class Meta:
        model = Wypozyczanie
        fields = '__all__'