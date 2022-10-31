import json
import googlemaps
from datetime import datetime
from datetime import timedelta
import polyline
import pyowm


def get_route(startLoc,endLoc):
    gmaps = googlemaps.Client(key='AIzaSyCVNClwrqUgwjzd-aRcCWNozH9JXWW4nKg')
    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions(startLoc,
                                         endLoc,
                                         mode="driving",
                                         departure_time=now)
    segNum = len(directions_result[0]['legs'][0]['steps'])
    infoList =[]
    timeStampTot = 0
    for i in range(0,segNum):
        lat = directions_result[0]['legs'][0]['steps'][i]['start_location']['lat']
        lon = directions_result[0]['legs'][0]['steps'][i]['start_location']['lng']
        polyLine =  directions_result[0]['legs'][0]['steps'][i]['polyline']['points']
        latlonSeg = polyline.decode(polyLine)
        stTime = directions_result[0]['legs'][0]['steps'][i]['duration']['text']
        listTime =  stTime.split(" ")  #List
        timecompNum = len(listTime)
        for ii in range(1,timecompNum,2):
            timeStampSeg=0
            if listTime[ii] in ['days', 'day']:
                timeStampSeg = int(listTime[ii-1])*86400
            if listTime[ii] in ['hours', 'hour']:
                timeStampSeg = timeStampSeg+int(listTime[ii-1])*3600
            if listTime[ii] in ['mins', 'min']:
                timeStampSeg = timeStampSeg+int(listTime[ii-1])*60
            timeStampTot = timeStampSeg+timeStampTot
# <<<<<<< HEAD
    thisList = {'lat':lat, 'lon':lon, 'timeStamp':timeStampTot,'polyline':polyline}
    infoList.append(thisList)
# =======
    thisList = {'lat':lat, 'lon':lon, 'timeStamp':timeStampTot}
    infoList.append(thisList)
# >>>>>>> 0fbaee2cd9bdd2d014b322b4e9f2ac691f6a0a13
    return infoList


testList = (get_route("San Francisco","New york"))
# <<<<<<< HEAD


for i in testList:
            print i.get('polyline')
# =======
#for i in testList:
#    print i.get('lat')
# >>>>>>> 0fbaee2cd9bdd2d014b322b4e9f2ac691f6a0a13
