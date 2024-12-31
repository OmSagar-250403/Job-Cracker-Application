from django.shortcuts import render
from templates import *

def login_page(request):
    return render(request, 'accounts/login.html')
