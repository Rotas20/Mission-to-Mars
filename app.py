
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo


app = Flask(__name__)


conn = "mongodb://localhost:27017/mars_app"
mars_db = pymongo.MongoClient(conn)



@app.route("/")
def index():
    renderData = mars_db.db.mars_data.find_one()
    print(renderData["MarsHemispheres"])
    return render_template("/index.html", mars=renderData)
   

@app.route("/scrape")
def functionScrape():

    mars_data = mars_db.db.mars_data
    mars_dict = scrape_mars.scrapeAll() 
    mars_data.replace_one({}, mars_dict, upsert=True)
    return redirect ("/", 302)

  
if __name__ == "__main__":
    app.run(debug=True)
