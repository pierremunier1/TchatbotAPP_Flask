import re
import unicodedata
import requests
from random import choice
import os

import config


class Parser:
    """class contains method to parse the user text input form"""

    def __init__(self, analyse):
        """initialising attribute"""

        self.analyse = analyse

    def parse(self):
        """method analyse the text and transform if necessary"""

        # switch to lower case
        self.analyse = self.analyse.lower()

        # remove accent
        self.analyse = ''.join((c for c in unicodedata.normalize
                                ('NFD', self.analyse)
                                if unicodedata.category(c) != 'Mn')
                               )

        # remove punctuation
        self.analyse = re.sub(r"[.!,;?\']", " ", self.analyse).split()

        # check stopword
        self.analyse = [x for x in self.analyse if x not in config.STOPWORDS]

        # to convert the list to string.
        self.analyse = ' '.join(self.analyse)

        return self.analyse


class GoogleApi:
    """classe contains method for geocoding api"""

    def __init__(self, userQuery):
        """initializing instance attributes"""

        self.user_query = userQuery
        self.latitude = float
        self.longitude = float
        self.global_address = str

    def position(self):
        """method find the correct position with geocoding google api"""

        payload = {
            'address': self.user_query,
            'key': os.environ.get('API_KEY_BACK')}
        result = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json',
            params=payload)
        google_maps = result.json()
        status = google_maps['status']

        if status == 'OK':
            self.latitude = (
                google_maps['results'][0]['geometry']['location']['lat']
                )
            self.longitude = (
                google_maps['results'][0]['geometry']['location']['lng']
                )
            self.global_address = (
                google_maps['results'][0]['formatted_address']
                )

            return self.latitude, self.longitude, self.global_address


class WikiApi:
    """class contain all methods to retreive data from mediawiki api"""

    def __init__(self, latitude, longitude):
        """ Initializing instance attribute """

        self.latitude = latitude
        self.longitude = longitude

    def get_wiki(self):
        """get wikipedia articles from mediawiki api in two step"""

        geo = '{}|{}'.format(self.latitude, self.longitude)

        payload = {'format': 'json',
                   'action': 'query',
                   'list': 'geosearch',
                   'gsradius': 50,
                   'gscoord': geo}

        result = requests.get(
            'https://fr.wikipedia.org/w/api.php',
            params=payload)

        # second step if statut code is ok, retreive all details of the
        # selected articles

        if result.status_code == 200:
            media_wiki = result.json()

            pageid = media_wiki['query']['geosearch'][0]['pageid']

            payload = {'format': 'json',
                       'action': 'query',
                       'prop': 'extracts|info',
                       'inprop': 'url',
                       'exchars': 300,
                       'explaintext': 1,
                       'pageids': pageid}

            result = requests.get(
                'https://fr.wikipedia.org/w/api.php',
                params=payload)

            extract_wiki = result.json()

            url = extract_wiki['query']['pages'][str(pageid)]['canonicalurl']
            extract = extract_wiki['query']['pages'][str(pageid)]['extract']

            return extract, url


class Grandpy:
    """give a random response"""

    def reply():
        """when the place is correct,
             give an response"""

        answer = choice(config.LISTREPLY)
        return answer

    def reply_noanswer():
        """when the place is incorrect,
            give an random response"""

        noanswer = choice(config.LISTNOREPLY)
        return noanswer


class Response:
    """analyse and return response"""

    def response_front(usertext):
        """return response to the front-end"""

        analyse = Parser(usertext)
        userQuery = analyse.parse()
        query = GoogleApi(userQuery)
        userQuery = query.position()
        addressCoords = query.position()

        try:
            latitude = addressCoords[0]
            longitude = addressCoords[1]
            globalAddress = addressCoords[2]
            coords = WikiApi(latitude, longitude)
            extract = coords.get_wiki()[0]
            url = coords.get_wiki()[1]
            response = Grandpy.reply()

        except BaseException:
            latitude = ''
            longitude = ''
            globalAddress = ''
            extract = ''
            url = ''
            response = Grandpy.reply_noanswer()

        result = {'lat': latitude,
                  'lng': longitude,
                  'globalAddress': globalAddress,
                  'user': usertext,
                  'extract': extract,
                  'url': url,
                  'response': response}
        
        return result
