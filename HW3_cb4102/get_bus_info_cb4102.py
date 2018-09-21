
import sys
import json
import os
import csv
import pylab as pl
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


key = sys.argv[1]
bus_line = sys.argv[2]
file_name = sys.argv[3]

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + key + '&LineRef=' + bus_line

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

data1 = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

with open(file_name, "w",newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['latitude','longitude','Stop Name','Stop Status'])
    for i in data1:
        latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        stop_name =  i['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
        stop_status = i['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
        writer.writerow([latitude,longitude,stop_name,stop_status])
