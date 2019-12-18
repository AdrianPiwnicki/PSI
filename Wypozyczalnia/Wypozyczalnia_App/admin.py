from django.contrib import admin
from .models import Klient
admin.site.register(Klient)

from .models import Pracownik
admin.site.register(Pracownik)

from .models import Samochód
admin.site.register(Samochód)

from .models import Wypożyczanie
admin.site.register(Wypożyczanie)

# Register your models here.