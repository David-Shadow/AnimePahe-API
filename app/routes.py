from flask import jsonify
from app import app
from app.controllers.pahe import pahe

@app.route('/')
def home():
    return "Welcome to Thee Mikey's API!"

app.register_blueprint(pahe, url_prefix='/pahe')