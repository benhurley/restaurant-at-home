from flask import Flask

app = Flask(__name__)

@app.route('/')
def restaurant_list():
    return "restaurant list"