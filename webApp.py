from flask import Flask
from flask import request
from flask import render_template
import pymysql.cursors

# FLASK APP NAME
app = Flask(__name__)

@app.route("/")
def main():
    # MYSQL DATABASE CONNECTION
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="topCharts",
        cursorclass=pymysql.cursors.DictCursor)

    # TRY TO RETRIEVE DATA STORED IN 'TOPCHARTS' DATABASE
    cur = mydb.cursor()

    try:
        with cur as cursor:
            query = "SELECT * from artist_song"
            cur.execute(query)
            # FETCH THE RESULTS AS A LIST
            data = cur.fetchall()
            mydb.close()
            return render_template('index.html', data=data)
    except Exception as e:
        return 'ok'

# MAIN PROGRAM
if __name__ == "__main__":
    app.run()
