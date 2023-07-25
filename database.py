import mysql.connector
'''import requests
import re
from bs4 import *

URL = "https://www.latlong.net/category/hospitals-102-26.html"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup.prettify())
datas = soup.find_all("table")
 
# Iterate through all li tags
for data in datas:
    # Get text from each tag
    print(data.text)
for link in soup.find_all('a', 
                          attrs={'href': re.compile("^https://")}):
    # display the actual urls
    print(link.get('href'))  

'''


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="deens123",
  autocommit=True
)

mycursor=mydb.cursor()

def initializing():
  mycursor.execute("create database if not exists hospitals ;")
  mycursor.execute("use hospitals;")
  mycursor.execute("create table hos (name varchar(500),lat varchar(100),lon varchar(100));")
  mycursor.execute("insert into hos values('manipal hospital bangalore','12.958808','77.649141');")
  mycursor.execute("insert into hos values('Victoria hospital','12.9580295012','77.5709560495');")
  mycursor.execute("insert into hos values('ESI Hospital','12.9900215','77.55323450000003');")
  mycursor.execute("insert into hos values('Banglore Hospital','13.006752','77.561737');")
  mycursor.execute("insert into hos values('airforce hostpital','12.95801','77.63901');")

def values():
    mycursor.execute("use hospitals;")
    names=[]
    mycursor.execute("select name from hos;")
    o=mycursor.fetchall()
    for i in o:
        names.append(i[0])
    lat=[]
    mycursor.execute("select lat from hos;")
    o=mycursor.fetchall()
    for i in o:
        lat.append(i[0])
    lon=[]
    mycursor.execute("select lon from hos;")
    o=mycursor.fetchall()
    for i in o:
        lon.append(i[0])
    return names,lat,lon


