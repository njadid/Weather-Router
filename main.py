#!/usr/bin/env python
import pyowm
import datetime
import pytz
from get_route_segmented import get_route
from get_weather import get_weather
import pandas as pd
# Open Weather Map keys
owm = pyowm.OWM('2c03cbb93e1a3cefaa7550826ac968a5')

route_list=get_route("Iowa City", "Chicago")

#print route_list_and weathers
all_points = []
for i in range(0,len(route_list),200):
	point = route_list[i]
	wet_point = get_weather(point.get('lat'),point.get('lon'),point.get('timeStamp')+7200)
	all_points.append(wet_point)   # this is a list of dictionaries

df=pd.DataFrame(all_points)
df.to_csv('out.csv', sep=',')

##print df  ## pandas framework
