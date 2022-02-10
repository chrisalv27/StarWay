from django.shortcuts import render
from .models import Zodiac

from django.http import HttpResponse

def myview(request):
    return HttpResponse('hello world!')

def index(request):
    context = {
        'zodiac': Zodiac.objects.all()
        }
    return render(request, 'starway_app/index.html', context)

def find_sign(request):
    sign = request.POST.get('sign')


# Create your views here.
