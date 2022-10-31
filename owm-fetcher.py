import pyowm
import datetime
<<<<<<< HEAD


owm = pyowm.OWM('1e873eee78c930746e6d9cd134ded491')


def get_weather(lat, lon, dt):  # time only in seconds and time from now
    "get the weather at lat lon time"
    time = datetime.datetime.utcnow() + datetime.timedelta(seconds=dt)
    print "what time is it now?"
    print datetime.datetime.utcnow()
    print time
    raw_data = owm.three_hours_forecast_at_coords(lat, lon)
    time
    wet_obj = raw_data.get_weather_at(time)
    ##next_time     = time + datetime.timedelta(minutes=179)
    return wet_obj


a = get_weather(53, -113.47, 10800)
print a.get_reference_time(timeformat='date')
#####
=======
import pytz
#from get_route import get_route
from get_route_segmented import get_route
from get_weather import get_weather
import pandas as pd
#owm = pyowm.OWM('1e873eee78c930746e6d9cd134ded491')
#owm = pyowm.OWM('0335868d22912afe8795d94e5d841e37')
owm = pyowm.OWM('2c03cbb93e1a3cefaa7550826ac968a5')


def df_to_geojson(df, properties, lat='lat', lon='lon'):
    geojson = {'type':'FeatureCollection', 'features':[]}
    for _, row in df.iterrows():
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}
        feature['geometry']['coordinates'] = [row[lon],row[lat]]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    return geojson
>>>>>>> 0fbaee2cd9bdd2d014b322b4e9f2ac691f6a0a13


route_list=get_route("Vancouver", "Chicago")


#print route_list
all_points = []
for i in range(0,len(route_list),200):
	#print i
	point = route_list[i]
	#for point in route_list:
	#print point
	wet_point = get_weather(point.get('lat'),point.get('lon'),point.get('timeStamp')+7200)
	#wet_dict  = wet_to_dict(wet_point)
	###*****
	#get_dict_weather
	#pres_dict = a.get_pressure()
	#pres      = pres_dict['press']
	#print a.get_reference_time(timeformat='date')
	#print "*********"
	#print point.get('lat')
	#print point.get('lon')
	#dt = point.get('timeStamp')
	#print dt
	#print datetime.datetime.utcnow() + datetime.timedelta(seconds=dt)
	#print 'humidity is :'+ str(a.get_humidity())
	#print 'pressure is :'+ str(pres)
	#print '****'
	all_points.append(wet_point)	

df=pd.DataFrame(all_points)
print('We have {} rows'.format(len(df)))
#print df
print df
print str(df.columns.tolist())
df['lat'] = df['lat'].astype(float)
df['lon'] = df['lon'].astype(float)
#print all_points
cols = ['temp', 'humidity']
gjason = df_to_geojson(df, cols)
#print gjason
#####
exit()

### this is all the forecasts
lat = 53.55
lon = -113.47
met_data = owm.three_hours_forecast_at_coords(lat, lon)
# 40 forecast objects every three hours #print(bb.get_forecast().count_weathers())
forecast_data = met_data.get_forecast()
# print forecast_data.get_location()
weathers = forecast_data.get_weathers()

for i in range(0, 39):
    wet_now = weathers[i]
    # print wet_now.get_humidity()
    time = wet_now.get_reference_time(timeformat='iso')
    rain_dict = wet_now.get_rain()
    snow_dict = wet_now.get_snow()

    if '3h' in rain_dict:
        rain = rain_dict['3h']
    else:
        rain = 0

    if '3h' in snow_dict:
        snow = snow_dict['3h']
    else:
        snow = 0
    temp_dict = wet_now.get_temperature(unit='celsius')
    temp = temp_dict['temp']
    wind_dict = wet_now.get_wind()
    wind_speed = wind_dict['speed']
    wind_dir = wind_dict['deg']
    humidity = wet_now.get_humidity()
    visibility = wet_now.get_visibility_distance()
    clouds = wet_now.get_clouds()
    status = wet_now.get_detailed_status()
    pres_dict = wet_now.get_pressure()
    pres = pres_dict['press']
    sea_lvl = pres_dict['sea_level']
    print "print time, rain, snow, temp, humidity, visibility, clouds, wind_dir, wind_speed	"
    print time, rain, snow, temp, humidity, visibility, clouds, wind_dir, wind_speed, status
# print visibility
# print pres, sea_lvl
###print ttemp['temp'] #print ttemp.values()[2]
exit()
