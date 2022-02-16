from django.shortcuts import render
from .models import Zodiac

from django.http import HttpResponse

def myview(request):
    return HttpResponse('hello world!')

def index(request):
    context = {
        'zodiac': Zodiac.objects.all()
        }
    return render(request, 'starway_app/starway.html', context)



# Create your views here.
