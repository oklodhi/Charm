from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql.cursors

# WEBPAGE CONNECTION
url = urlopen ("http://www.officialcharts.com/charts/singles-chart/")

# GRAB ARTIST AND TITLE
bsObj = BeautifulSoup(url, features="lxml")
recordList = bsObj.findAll("div", {"class" : "title-artist",})

# ITERATE OVER RECORDLIST TO GRAB ARTIST AND TITLE
for record in recordList:
     title = record.find("div", {"class": "title",}).get_text().strip()
     artist = record.find("div", {"class": "artist"}).get_text().strip()
     print (artist + ': ' + title)

