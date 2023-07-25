import json
import requests 
from ip2geotools.databases.noncommercial import DbIpCity
import geopy.distance

class distance():
    def distancegivenip(ip, listoflatlong):
        res = DbIpCity.get(ip, api_key="free")
        latlonguser = (res.latitude, res.longitude)
        distances = []
        for i in range(len(listoflatlong[0])):
 #           print(listoflatlong[0][i],listoflatlong[1][i],listoflatlong[2][i])
            distances.append({"Hospital-> ":listoflatlong[0][i], "Distance-> ": geopy.distance.geodesic(latlonguser, (listoflatlong[1][i],listoflatlong[2][i])).km})

        ples = [dictii["Distance-> "] for dictii in distances]
        minples = min(ples)
        final = [pair for pair in distances if pair["Distance-> "] == minples]
        return final

listlanglong = (['manipal hospital bangalore', 'Victoria hospital', 'ESI Hospital', 'Banglore Hospital', 'airforce hostpital'], ['12.958808', '12.9580295012', '12.9900215', '13.006752', '12.95801'], ['77.649141', '77.5709560495', '77.55323450000003', '77.561737', '77.63901'])
#print(distance.distancegivenip("122.167.187.56", listlanglong))