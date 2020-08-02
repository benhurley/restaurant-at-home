import json
from bson.json_util import dumps
from bson import ObjectId
from flask import Flask, request, jsonify
from test_data.restaurant_data import RESTAURANTS
from flask_pymongo import PyMongo

app = Flask(__name__, static_folder='../build', static_url_path='/')
app.config["MONGO_URI"] = "mongodb+srv://restaurantathome:omgpassword@cluster0.536qw.mongodb.net/restaurantathome?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
mongo = PyMongo(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

# Custom encoder for MongoDB (ObjectId class isn't serializable)
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route('/api/restaurants', methods=['GET'])
def get_all_restaurants():
    res=[]
    collection = mongo.db.restaurants.find()
    for doc in collection:
        res.append(doc)
    return JSONEncoder().encode(res)

# Takes a list of restaurants to add to the database
@app.route('/api/restaurants', methods=['POST'])
def add_restaurants():
    restaurants = mongo.db.restaurants
    body = request.get_json()
    to_insert = []
    for item in body:
        to_insert.append({
            'name' : item.get('name'),
            'playlist': item.get('playlist'),
            'lighting': item.get('lighting'),
            'scent': item.get('scent'),
            'tableItems': item.get('tableItems')
        })
    print(jsonify(to_insert))
    new_ids = restaurants.insert_many(to_insert)
    return JSONEncoder().encode(new_ids)
    

@app.route('/api/restaurants/<int:id>', methods = ['GET', 'POST', 'DELETE'])
def get_restaurants(id):
    if request.method == 'GET':
        return JSONEncoder().encode(mongo.db.restaurants.find_one({"id":id}))

    # if request.method == 'POST':

    # if request.method == 'DELETE':
    

