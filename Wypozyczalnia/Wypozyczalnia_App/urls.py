from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers


urlpatterns = [
    path('Klient', views.KlientList.as_view()),
    path('Klient/<int:pk>/', views.KlientDetail.as_view()),
    path('Samochod', views.SamochodList.as_view()),
    path('Samochod/<str:pk>/', views.SamochodDetail.as_view()),
    path('Pracownik', views.PracownikList.as_view()),
    path('Pracownik/<int:pk>/', views.PracownikDetail.as_view()),
    path('Wypozyczanie', views.WypozyczanieList.as_view()),
    path('Wypozyczanie/<int:pk>/', views.WypozyczanieDetail.as_view()),

]



urlpatterns = format_suffix_patterns(urlpatterns)
