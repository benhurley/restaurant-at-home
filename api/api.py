from flask import Flask, request, jsonify
from test_data.restaurant_data import RESTAURANTS

app = Flask(__name__)

@app.route('/api/restaurants')
def get_all_restaurants():
    return jsonify(list(RESTAURANTS))

@app.route('/api/restaurants/<int:id>')
def get_restaurants(id):
    if id is not None:
        return jsonify(list(filter(lambda restaurants, id=id: id == restaurants['id'], RESTAURANTS)))
    else:
        return list(RESTAURANTS)