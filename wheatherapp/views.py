from django.shortcuts import render
import json
import urllib.request
import math
# Create your views here.
def index(request):
    if request.method =="POST":
        city =request.POST['city']
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=9ce44628fdc6599119e350972b751f31').read()
        json_data=json.loads(res)
        data = {
            "country_code":str(json_data['sys']['country']),
            'coordinate':str(json_data['coord']['lon'])+ ' '+ str(json_data['coord']['lat']),
            'temp':str(math.floor(json_data['main']['temp'] - 273)),
            'pressure':str(json_data['main']["pressure"]),
            'humidity':str(json_data['main']['humidity']),
            "city": request.POST['city']

        }
    else:
        data = {}
    return render(request,"index.html", data )