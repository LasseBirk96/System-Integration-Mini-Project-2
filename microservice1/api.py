from __main__ import app
from flask import request
from microservice1 import api_methods

@app.route("/complain", methods=["POST"])
def user_sends_complaint():
    data = request.get_json()
    return api_methods.handle_user_complaint(data)
    
