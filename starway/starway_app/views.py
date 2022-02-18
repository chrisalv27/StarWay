from datetime import datetime
from xmlrpc.client import DateTime
from django.shortcuts import render
from .models import Zodiac, User



from django.http import HttpResponse



def getsign(request):
    if request.method == 'POST':
        birth = request.POST.get('birth')
        # name = ...get name somehow
        user = User.objects.create(birth=birth, name='Bob')
        print(user.name, user.birth)
        user_bday_2022 = user.birth.replace(year=2022)
        zodiacs = Zodiac.objects.all()
        for zodiac in zodiacs:
            print()
            print(zodiac.name)
            print(zodiac.start_date)# <= user_bday_2022)
            print(zodiac.end_date)# >= user_bday_2022)
            # if zodiac.name == 'Aquarius': # in your version it would be more like if user.birth is in the range
                                          # of the zodiac start and end dates
                # user.zodiac = zodiac
        return render(request, 'starway_app/starway.html')

def index(request):
    context = {
        'zodiac': Zodiac.objects.all()
        }
    return render(request, 'starway_app/starway.html', context)

# def year():
#     user = datetime.birth('birth')
#     replace = user.replace(year=2022)

# this is a helper function, it would be called in entry or whatever function needs it
# def check_dates(zodiac_start, zodiac_end, user_bday_2022):
#     """Takes in the starting date and ending date of a zodiac range,
#     as well as the user's 2022 birthday and returns True if the 2022
#     birthday falls in the range of those dates"""
#     ...




# Create your views here.
