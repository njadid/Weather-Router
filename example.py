import pyowm

owm = pyowm.OWM('1e873eee78c930746e6d9cd134ded491')
lat = 41.66
lon = -91.53

met_data       = owm.three_hours_forecast_at_coords(lat,lon)
# 40 forecast objects every three hours #print(bb.get_forecast().count_weathers())
forecast_data  = met_data.get_forecast()
forecast_data.get_temperature(unit="kelvin")
print forecast_data.get_location()
print forecast_data.get_weathers()
exit()
