#!flask/bin/python
from flask import Flask, render_template
from flask_restful import Api
from fashin import Fashin

app = Flask(__name__, static_folder="static")
api = Api(app)
api.add_resource(Fashin, '/api/fashin')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
