from .models import Klient, Samochód, Pracownik, Wypożyczanie
from rest_framework import serializers


class KlientSerializer(serializers.Serializer):
    class Meta:
        model = Klient
        fields = '__all__'


class SamochodSerializer(serializers.Serializer):
    class Meta:
        model = Samochód
        fields = '__all__'


class PracownikSerializer(serializers.Serializer):
    class Meta:
        model = Pracownik
        fields = '__all__'


class WypozyczanieSerializer(serializers.Serializer):
    class Meta:
        model = Wypożyczanie
        fields = '__all__'