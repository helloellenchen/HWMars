# Dependencies
from flask import Flask, jsonify, render_template, request
import pymongo
import scrape_mars
import datetime

app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.classDB
mars = db.mars.find_one()

@app.route("/")
def index():
    mars_info = db.mars.find_one()

    return render_template("templates/index.html", mars_dict=mars_dict)


@app.route("/scrape")
def scrape():
    mars_info = db.mars.find_one()
    mars_data = scrape_mars.Scrape()
    mars_info.update(
        {},
        mars_data,
        upsert = True
    )

    return index()

if __name__ == "__main__":
    app.run(debug=False)