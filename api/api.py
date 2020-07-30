import json
from bson import ObjectId
from flask import Flask, request, jsonify
from test_data.restaurant_data import RESTAURANTS
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://restaurantathome:<text me for password>@cluster0.536qw.mongodb.net/restaurantathome?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
mongo = PyMongo(app)

# Custom encoder for MongoDB (ObjectId class isn't serializable)
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route('/api/restaurants')
def get_all_restaurants():
    res=[]
    collection = mongo.db.restaurants.find()
    for doc in collection:
        res.append(doc)
    return JSONEncoder().encode(res)

@app.route('/api/restaurants/<int:id>')
def get_restaurants(id):
    return JSONEncoder().encode(mongo.db.restaurants.find_one({"id":id}))