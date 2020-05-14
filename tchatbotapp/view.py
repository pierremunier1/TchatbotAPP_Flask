from flask import render_template, jsonify, request
from . import tchatbotapp
from .utils import Parser, GoogleApi, WikiApi, Grandpy


class Front:
    """class contains all methods to display the data to the front"""

    @tchatbotapp.route('/')
    def index():
        return render_template('index.html')

    @tchatbotapp.route("/ajax", methods=["POST"])
    def ajax():
        """analyse the text entered in the user input"""

        request.method == "POST"
        usertext = request.form["usertext"]
        analyse = Parser(usertext)
        userQuery = analyse.parse()
        query = GoogleApi(userQuery)
        userQuery = query.position()

        try:
            addressCoords = query.position()
            latitude = addressCoords[0]
            longitude = addressCoords[1]
            globalAddress = addressCoords[2]
            coords = WikiApi(latitude, longitude)
            extract = coords.get_wiki()[0]
            url = coords.get_wiki()[1]
            response = Grandpy.reply()
            user = usertext

        except BaseException:
            latitude = ''
            longitude = ''
            globalAddress = ''
            user = ''
            extract = ''
            url = ''
            response = Grandpy.reply_noanswer()

        return jsonify({'lat': latitude,
                        'lng': longitude,
                        'globalAddress': globalAddress,
                        'extract': extract,
                        'url': url,
                        'response': response,
                        'user': usertext
                        })