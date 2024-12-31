from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    list = [
        {'name': 'John', 'age': 25},
        {'name': 'Cena', 'age': 34}
    ]
    return render(request, 'home.html', context={'peoples': list, 'page': 'Home'})
