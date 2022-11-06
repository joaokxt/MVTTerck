from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar

def familia(request):
    padre = Familiar(nombre='Davi', edad='46', nacimiento='1976-10-10')
    madre = Familiar(nombre = 'Renata', edad='44', nacimiento='1978-08-15')
    hermana = Familiar(nombre='Julia', edad='22', nacimiento='2000-03-24')
    dict_familia = {'objeto_1':padre,
                    'objeto_2':madre,
                    'objeto_3':hermana,
                    }
    return render(request, 'familia.html', dict_familia)
