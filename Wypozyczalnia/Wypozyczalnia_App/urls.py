from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('Klient', views.KlientList.as_view()),
    path('Klient/<int:pk>', views.KlientDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)