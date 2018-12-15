#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_Mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/Mission_To_Mars_App")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/")
def home():
    mars_ = mongo.db.mars_.find()
    return render_template("index.html", mars_=mars_)
   
@app.route("/scrape")
def scrape():
    mars_info = mongo.db.mars_info
    mars_info_data = scrape_mars.mars_scrapes()
    mars_info.update({}, mars_info_data, upsert=True)
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(debug=True)



# In[ ]:




