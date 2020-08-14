from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
	return render(request, 'generator/home.html', {'password': 'abcdef'})

def password(request):
    c = list('abcdefghijklmnopqrstuvwxyz')
    p = ''
    l = int(request.GET.get('length', 1))
    if request.GET.get('uppercase'):
        c.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        c.extend(list('0123456789'))
    if request.GET.get('special'):
        c.extend(list('!@#$%^&*'))
    for i in range(l):
        p = p + random.choice(c)
    return render(request, 'generator/password.html', {'password': p})

def about(request):
    return render(request, 'generator/about.html')
