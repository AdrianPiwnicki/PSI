from django.http import HttpResponse

def index(request):
    return HttpResponse("Witaj swiecie. Oto widok defaultowy.")
