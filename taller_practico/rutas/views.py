from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test1(request):
    return HttpResponse("<h1>Hola mundo con las #manosenelcódigo</h1>")


def test2(request):
    return HttpResponse("<h1>Hola desde Test 2</h1>")


def parametro1(request, id):
    return HttpResponse(f"<h1>Hola desde Parámetro 1</h1><h2>{id}</h2>")


def parametro2(request, id1, id2):
    return HttpResponse(f"<h2>{id1}</h2><h2>{id2}</h2>")
