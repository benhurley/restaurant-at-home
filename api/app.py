import os
from flask import Flask, request, send_from_directory
from restaurant_data import RESTAURANTS

app = Flask(__name__, static_folder='restaurant-at-home/build')

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)

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
