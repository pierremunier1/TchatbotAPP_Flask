from flask import render_template, jsonify, request ,json
from . import tchatbotapp
from .utils import Parser, GoogleApi ,WikiApi

class Front:

    
    @tchatbotapp.route('/')
    def index():
        return render_template('index.html')

   
    @tchatbotapp.route("/ajax", methods=["POST","GET"])
    def ajax():

            if request.method == "POST":
                usertext = request.form["usertext"]
                analyse = Parser(usertext)
                userQuery = analyse.parse()
                query = GoogleApi(userQuery)
                userQuery = query.position()
                # Running the history method to get the wikipedia page for that coordonates.
                addressCoords = query.position()
                latitude = addressCoords[0]
                longitude = addressCoords[1]
                globalAddress = addressCoords[2]
                coords = WikiApi(latitude, longitude)
                wikiExtract = coords.get_wiki()[0]
                print(wikiExtract)
                pageid = coords.get_wiki()[1]    
                return json.dumps({'userText': userQuery, \
                                    #'addressAnswer': addressAnswer, \
                                    'lat':latitude, \
                                    'lng':longitude, \
                                    'globalAddress':globalAddress, \
                                    #'storyAnswer': storyAnswer, \
                                    'wikiExtract': wikiExtract, \
                                    'pageid': pageid})