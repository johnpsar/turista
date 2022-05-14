from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .cf.add_rating_2_csv import addNewRating
from helper.dataProcessing import dataExtract


class PointOfInterest:
    def __init__(self, id, name, mapsLink):
        self.id = id
        self.name = name
        self.mapsLink = mapsLink

    def dump(self):
        return {"Poi": {'id': self.id,
                        'name': self.name,
                        'mapsLink': self.mapsLink}}


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def getAll(request):
    places = ["Athens", "Rome", "Paris"]
    return JsonResponse(places, safe=False)

@ csrf_exempt
def getRoute(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    place = body["place"]
    
    count = body["count"]
    recommendations_selected = body["recommendations_selected"]
    route = addNewRating(recommendations_selected, place)
    myroute=[]
    for re in route:
        myroute.append({"id":str(re[0]),"name":str(re[1]),"url":str(re[2]),"type":str(re[3]),"idk":str(re[4]),"path":str(re[5]),"desc":str(re[6])})
    # route = []
    # route.append({"id": "1", "name": "Acropolis", "url": "www.google.com"})
    # route.append({"id": "2", "name": "Spiti Makri", "url": "www.google.com"})
    # route.append({"id": "3", "name": "Spiti Evas", "url": "www.google.com"})
    # route.append({"id": "4", "name": "Greafeia Turista",
    #              "url": "www.google.com"})
    # route.append({"id": "5", "name": "Spiti Gerasimou",
    #              "url": "www.google.com"})
    # route.append({"id": "6", "name": "Psarrospiti", "url": "www.google.com"})

    # routeJSON = json.dumps([o.dump() for o in route], indent=3)


    return JsonResponse(myroute, safe=False)


def changeOption(request, image_id):

    return JsonResponse("Changing image with id:%s  ", image_id)


@ csrf_exempt
def getWeather(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    date = body['date']
    place=body['place']
    data = dataExtract(date,place)
    isRainNow = data[0]
    isRainLater = data[1]
    isWindNow = data[2]
    isWindLater = data[3]
    tempNow = data[4]
    tempLater = data[5]
    weatherNow = ""
    weatherLater = ""
    if(isRainNow and isWindNow):
        weatherNow = "rain"
    elif (isRainNow and not isWindNow):
        weatherNow = "rain"
    elif(not isRainNow and isWindNow):
        weatherNow = "wind"
    else:
        weatherNow = "sun"

    if(isRainLater and isWindLater):
        weatherLater = "rain"
    elif (isRainLater and not isWindLater):
        weatherLater = "rain"
    elif(not isRainLater and isWindLater):
        weatherLater = "wind"
    else:
        weatherLater = "sun"
    
    weather = []
    weather.append({"condition": weatherNow, "temperature": tempNow})
    weather.append({"condition": weatherLater, "temperature": tempLater})
    return JsonResponse(weather, safe=False)

