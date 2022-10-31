import json
import googlemaps
from datetime import datetime
#from datetime import timedelta
import polyline

##NO TIME COMPONENT

#Input: Origin, destination, time
#Output: infoList (lat lon deltime)
def get_route(startLoc,endLoc):
    gmaps = googlemaps.Client(key='AIzaSyCVNClwrqUgwjzd-aRcCWNozH9JXWW4nKg')
    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions(startLoc,
                                         endLoc,
                                         mode="driving",
                                         departure_time=now)
    segNum = len(directions_result[0]['legs'][0]['steps'])
    print segNum
    infoList =[]
    timeStampTot = 0
    all_points = []
    this_seg = []
    for i in range(0,segNum):
        lat = directions_result[0]['legs'][0]['steps'][i]['start_location']['lat']
        lon = directions_result[0]['legs'][0]['steps'][i]['start_location']['lng']
        stTime = directions_result[0]['legs'][0]['steps'][i]['duration']['text']
        listTime =  stTime.split(" ")  #List
        polyLine =  directions_result[0]['legs'][0]['steps'][i]['polyline']['points']
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
        latlonSeg = polyline.decode(polyLine)
        latlonLen = len(latlonSeg)
        #thistimeStamp = [jj for jj in range(latlonLen)]
        for ii in range(0,latlonLen):
            thislat = latlonSeg[ii][0]
            thislon = latlonSeg[ii][1]
            thistimeStamp = timeStampTot
            thispoint = {'lat': thislat, 'lon': thislon, 'timeStamp': thistimeStamp} #change this
            print thispoint
            all_points.append(thispoint)

    return all_points

testList = (get_route("Iowa City", "Chicago"))
#print(testList)

