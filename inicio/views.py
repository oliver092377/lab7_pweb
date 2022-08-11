from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs): 
    '''
    *N° variables indeterminados de argumentos
    **Recibir argumentos que pueden ser iterados
    '''
    #return HttpResponse('<h1>Hello DEAR~</h1>')
    return render(request, 'home.html', {})