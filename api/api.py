from flask import Flask
from test_data.restaurant_data import RESTAURANTS

app = Flask(__name__)

@app.route('/restaurants')
def get_current_time():
    results = []
    for n in RESTAURANTS:
        results.append(n)

    return {'restaurants': results}