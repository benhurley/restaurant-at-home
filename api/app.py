from flask import Flask, request, send_file
from restaurant_data import RESTAURANTS

app = Flask(__name__)

@app.route('/')
def root():
    return send_file('/build/index.html')

@app.route('/api/restaurants')
def get_restaurants():
    results = []

    if 'id' in request.args:
        id = request.args['id']
        for n in RESTAURANTS:
            if str(n['id']) == id:
                results.append(n)
    else:
        for n in RESTAURANTS:
            results.append(n)
    
    return {'restaurants': results}
