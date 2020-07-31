from flask import Flask, request

app = Flask(__name__, static_folder='../build', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

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

RESTAURANTS = [
    {
        "id": 1,
        "name": "Joe's Italian Restaurant",
        "playlist": "Italian Cooking Music",
        "lighting": "80%",
        "scent": "vanilla candles",
        "tableItems": [ "cloth napkins", "salt", "pepper", "chili peppers", "olive oil", "silverware" ],
    },
    {
        "id": 2,
        "name": "Jane's Ramen Spot",
        "playlist": "Top 50 USA",
        "lighting": "60%",
        "scent": "palo santo sticks",
        "tableItems": [ "chop sticks," "paper napkins", "cayenne", "sake" ],
    },
    {
        "id": 3,
        "name": "49 Club Steakhouse",
        "playlist": "Frank Sinatra",
        "lighting": "50%",
        "tableItems": [ "silverware," "steak sauce", "salt", "pepper", "wine bottle holder", "toothpicks" ],
    },
    {
        "id": 4,
        "name": "ATK",
        "playlist": "Deep Hau5",
        "lighting": "40%",
        "tableItems": [],
    },
    {
        "id": 5,
        "name": "Dumplings 2 Go",
        "playlist": "Easy Listening",
        "lighting": "20%",
        "tableItems": ["soy sauce", "napkins"],
    },
]
