from datetime import datetime
from xmlrpc.client import DateTime
from django.shortcuts import render
from .models import Zodiac, User



from django.http import HttpResponse



def getsign(request):
    if request.method == 'POST':
        birth = request.POST.get('birth')
        # name = request.POST.get('name')
        user = User.objects.create(birth=birth, name='bob')
        
        temp_date = user.birth
        temp_year = '2022-'
        for i in range(5,10):
            temp_year += temp_date[i]
        
        day = user.birth[8] + user.birth[9] #using indices of the day colum, concatinate them into day ex. "07"
        day = int(day) #typecast day string into an integer, to compare it with greater than or less than
        if user.birth[5] == "0" and user.birth[6] == "1":
                if day < 20:
                    user.zodiac = Zodiac.objects.get(name='Capricorn')
                elif day >= 20:
                    user.zodiac = Zodiac.objects.get(name='Aquarius')
        if user.birth[5] == "0" and user.birth[6] == "2":
                if day < 18:
                    user.zodiac = Zodiac.objects.get(name='Aquarius')
                elif day >= 18:
                    user.zodiac = Zodiac.objects.get(name='Pisces')
        if user.birth[5] == "0" and user.birth[6] == "3":
                if day < 20:
                    user.zodiac = Zodiac.objects.get(name='Pisces')
                elif day >= 20:
                    user.zodiac = Zodiac.objects.get(name='Aries')
        if user.birth[5] == "0" and user.birth[6] == "4":
                if day < 19:
                    user.zodiac = Zodiac.objects.get(name='Aries')
                elif day >= 19:
                    user.zodiac = Zodiac.objects.get(name='Taurus')
        if user.birth[5] == "0" and user.birth[6] == "5":
                if day < 20:
                    user.zodiac = Zodiac.objects.get(name='Taurus')
                elif day >= 20:
                    user.zodiac = Zodiac.objects.get(name='Gemini')
        if user.birth[5] == "0" and user.birth[6] == "6":
                if day < 21:
                    user.zodiac = Zodiac.objects.get(name='Gemini')
                elif day >= 21:
                    user.zodiac = Zodiac.objects.get(name='Cancer')
        if user.birth[5] == "0" and user.birth[6] == "7":
                if day < 22:
                    user.zodiac = Zodiac.objects.get(name='Cancer')
                elif day >= 22:
                    user.zodiac = Zodiac.objects.get(name='Leo')
        if user.birth[5] == "0" and user.birth[6] == "8":
                if day < 22:
                    user.zodiac = Zodiac.objects.get(name='Leo')
                elif day >= 22:
                    user.zodiac = Zodiac.objects.get(name='Virgo')
        if user.birth[5] == "0" and user.birth[6] == "9":
                if day < 22:
                    user.zodiac = Zodiac.objects.get(name='Virgo')
                elif day >= 22:
                    user.zodiac = Zodiac.objects.get(name='Libra')
        if user.birth[5] == "1" and user.birth[6] == "0":
                if day < 23:
                    user.zodiac = Zodiac.objects.get(name='Libra')
                elif day >= 23:
                    user.zodiac = Zodiac.objects.get(name='Scorpio')
        if user.birth[5] == "1" and user.birth[6] == "1":
                if day < 22:
                    user.zodiac = Zodiac.objects.get(name='Scorpio')
                elif day >= 22:
                    user.zodiac = Zodiac.objects.get(name='Sagittarius')
        if user.birth[5] == "1" and user.birth[6] == "2":
                if day < 21:
                    user.zodiac = Zodiac.objects.get(name='Sagittarius')
                elif day >= 21:
                    user.zodiac = Zodiac.objects.get(name='Capricorn')
                    
        user.save() # this actually writes the changes to the database
                
        
        return render(request, 'starway_app/starway.html')
    

def index(request):
    context = {
        'zodiac': Zodiac.objects.all(),
        
        }
    
    return render(request, 'starway_app/starway.html', context)






# Create your views here.
