import json
from bson.json_util import dumps
from bson import ObjectId
from flask import Flask, request, jsonify
from flask.json import JSONEncoder
from test_data.restaurant_data import RESTAURANTS
from flask_pymongo import PyMongo

# Custom encoder for MongoDB (ObjectId class isn't serializable)
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__, static_folder='../build', static_url_path='/')
app.config["MONGO_URI"] = "mongodb+srv://restaurantathome:omgpassword@cluster0.536qw.mongodb.net/restaurantathome?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
mongo = PyMongo(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/restaurants', methods=['GET', 'POST'])
def add_restaurants():

    # Gets all restaurants in the database
    if request.method == 'GET':
        res=[]
        collection = mongo.db.restaurants.find()
        for doc in collection:
            res.append(doc)
        return dumps(res)

    # Takes a list of restaurants to insert into the database
    if request.method == 'POST':
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
        new_ids = restaurants.insert_many(to_insert)
        return jsonify(str(new_ids))
    

@app.route('/api/restaurants/<str:id>', methods=['GET', 'POST', 'DELETE'])
def get_restaurants(id):
    if request.method == 'GET':
        return dumps(mongo.db.restaurants.find_one({"id":id}))

    elif request.method == 'DELETE':
        id = request.args.get('_id')
        print(id)
        restaurants = mongo.db.restaurants
        return restaurants.delete_one(id)


