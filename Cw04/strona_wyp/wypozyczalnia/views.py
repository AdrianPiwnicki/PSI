from django.http import HttpResponse

def index(request):
    return HttpResponse("Witaj świecie, napis testowy do wypożyczalni.")
