from django.shortcuts import render


def home_inicio(request):
    texto = "Mi mamá me los compró"
    return render(request, 'home/home.html', {'texto': texto})