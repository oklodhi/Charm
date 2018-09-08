from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql.cursors


def run():
    # CONNECT TO OFFICIALCHARTS WEB PAGE
    url = urlopen("http://www.officialcharts.com/charts/singles-chart/")

    # GRAB ARTIST AND TITLE
    bsObj = BeautifulSoup(url, features="lxml")
    recordList = bsObj.findAll("div", {"class": "title-artist", })
    recordRank = bsObj.findAll("span", {"class": "position", })

    # ITERATE OVER RECORDLIST TO GRAB ARTIST AND TITLE
    for record in recordList:
        title = record.find("div", {"class": "title"}).get_text().strip()
        artist = record.find("div", {"class": "artist"}).get_text().strip()
        print(artist + ': ' + title)

    # MYSQL DATABASE CONNECTION
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="topCharts",
        cursorclass=pymysql.cursors.DictCursor)

    # TRY TO INSERT ITEMS INTO DATABASE TABLE 'ARTIST_SONG'
    try:
        with mydb.cursor() as cursor:
            for record in recordList:
                title = record.find("div", {"class": "title"}).get_text().strip()
                artist = record.find("div", {"class": "artist"}).get_text().strip()
                sql = "INSERT INTO artist_song (artist, song) VALUEs (%s, %s)"
                cursor.execute(sql, (artist, title))
            mydb.commit()
    finally:
        mydb.close()

    print("\nRecord inserted.")
