
import sys
import os
from flask import Flask
from flask_restful import Api
sys.path.append("..")
app = Flask(__name__)
api = Api(app)

from microservice1 import api


@app.route("/home", methods=["GET"])
def home():
    return "<h1>HVIS DU SER DETTE SÅ KØRER DET</h1>"






if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)