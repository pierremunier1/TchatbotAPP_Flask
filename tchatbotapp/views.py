from flask import render_template, jsonify, request
from . import tchatbotapp
from .utils import Parser, GoogleApi, WikiApi, Grandpy, Response
import os


"""class contains all methods to display the data to the front"""

@tchatbotapp.route('/')
def index():
    return render_template('index.html',API_KEY=os.environ.get('API_KEY'))

@tchatbotapp.route("/ajax", methods=["POST"])
def ajax():
    """analyse the text entered in the user input"""

    usertext = request.form["usertext"]
    user_text = Response.response_front(usertext)
    
    return jsonify(user_text)
                    