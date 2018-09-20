
#import necessary libraries
import sys
import json
import os
import pylab as pl
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


key = sys.argv[1]
bus_line = sys.argv[2]


#key = 'ed535267-cb15-4347-9418-f4c376d09bdb'
#bus_line = 'B38'

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + key + '&LineRef=' + bus_line

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

data1 = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print("Bus Line : ", bus_line)
print("Number of active buses: ", len(data1))

for i in data1:
    lat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    lon = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus ", data1.index(i), "is at latitude", lat, "and longitude ", lon)
