from django.contrib import admin
from .models import Klient
admin.site.register(Klient)

from .models import Pracownik
admin.site.register(Pracownik)

from .models import Samochod
admin.site.register(Samochod)

from .models import Wypozyczanie
admin.site.register(Wypozyczanie)

# Register your models here.