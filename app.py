# ensure your MongoDB is running
# ensure you have a terminal open so you can run your server from.
# Dependencies and Setup
from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars

# need to set up flask and connection to MongoDB
app = Flask(__name__)


# use pymongo to establish mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")




# create route that renders index.html
# getting the data out of the db and passing the data to index.html
@app.route("/")
def home():
    mars=mongo.db.mars.find_one()
    
    return render_template("index.html",mars=mars)

# Scrape route to MongoDB 
@app.route("/scrape")
def scrape():
    mars=mongo.db.mars
    # this will take the data from the dictionary at the bottom of scrape_mars and return it to here and put it in the mongo database
    mars_data = scrape_mars.scrape()
    mars.update({},mars_data,upsert=True)

    return redirect("/")

if __name__ == "__main__":
        app.run(debug=True)

