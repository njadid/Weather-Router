import pyowm
import datetime
import pytz
#from get_route import get_route
from get_route_segmented import get_route
import pandas as pd
#owm = pyowm.OWM('1e873eee78c930746e6d9cd134ded491')
#owm = pyowm.OWM('0335868d22912afe8795d94e5d841e37')
owm = pyowm.OWM('2c03cbb93e1a3cefaa7550826ac968a5')


def get_weather(lat, lon, dt):    # time only in seconds and time from now
    """get the weather at lat lon time"""
    dt =dt +7200
    time = datetime.datetime.utcnow() + datetime.timedelta(seconds=dt)
    #print "what time is it now?"
    #print datetime.datetime.utcnow()
    raw_data      = owm.three_hours_forecast_at_coords(lat,lon)
    wet_obj       = raw_data.get_weather_at(time)
    ##next_time     = time + datetime.timedelta(minutes=179)
    #return wet_obj
    #####def wet_to_dict(wet_obj):
    time      = wet_obj.get_reference_time(timeformat='iso')
    rain_dict = wet_obj.get_rain()
    snow_dict = wet_obj.get_snow()

    if '3h' in rain_dict:
        rain = rain_dict['3h']
    else:
        rain = 0

    if '3h' in snow_dict:
        snow = snow_dict['3h']
    else:
        snow = 0
    temp_dict = wet_obj.get_temperature(unit='celsius')
    temp 	  = temp_dict['temp']
    wind_dict = wet_obj.get_wind()
    wind_speed= wind_dict['speed']
    wind_dir  = wind_dict['deg']
    humidity  = wet_obj.get_humidity()
    visibility= wet_obj.get_visibility_distance()
    clouds    = wet_obj.get_clouds()
    status    = wet_obj.get_detailed_status()
    pres_dict = wet_obj.get_pressure()
    pres      = pres_dict['press']
    sea_lvl   = pres_dict['sea_level']
    ###bools
    sun_bool  = raw_data.will_be_sunny_at(time)
    rain_bool = raw_data.will_be_rainy_at(time)
    snow_bool = raw_data.will_be_snowy_at(time)
    storm_bool = raw_data.will_be_stormy_at(time)
    tornado_bool = raw_data.will_be_tornado_at(time)
    hurricane_bool = raw_data.will_be_hurricane_at(time)
    fog_bool      = raw_data.will_be_foggy_at(time)
    #print sun_bool, rain_bool, snow_bool, storm_bool
    
    wet_dict  = {'lat': lat ,'lon':lon , 'time':time ,\
    'rain':rain , 'snow':snow , 'temp': temp , 'wind_speed':wind_speed ,\
    'wind_deg':wind_dir, 'humidity' : humidity , 'visibility' : visibility,\
    'clouds' : clouds , 'status' : status, 'pres' : pres,\
    'sun_bool': sun_bool , 'rain_bool':rain_bool, 'snow_bool':snow_bool, \
    'storm_bool' : storm_bool,'tornado_bool':tornado_bool, 'hurricane_bool':hurricane_bool, 'fog_bool':fog_bool
    }
    
    return wet_dict
