from flask import Flask, render_template, request
import get_weather
import os
import yelp_api
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
app = Flask(__name__)

@app.route('/')

def index():
    name = request.values.get('name')
    return render_template ('index.html', name=name)
    

@app.route('/about')

def about():
    return render_template('about.html')


@app.route('/weather')
def weather():
    address= request.values.get('address')
    forecast= None
    if address: 
        forecast= get_weather.weather(address)
    return render_template ('weather.html', forecast=forecast)


@app.route('/yelp')
def yelp():
    address= request.values.get('address')
    term = request.values.get('term')
    businesses= None
    if address and term: 
        businesses= yelp_api.yelp_lookup(address,term)
    return render_template('yelp.html', businesses=businesses)



if __name__ == "__main__":
    app.run()



