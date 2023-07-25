import json
import requests 
from ip2geotools.databases.noncommercial import DbIpCity

class distance():
    def distancegivenip(ip, listoflatlong):
        res = DbIpCity.get(ip, api_key="free")
        print(res.latitude, res.longitude)

distance.distancegivenip("103.162.212.2", [])

print("oooo")