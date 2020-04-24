import config

import re
import unicodedata
import requests


class Parser:

    def __init__(self,analyse):

        self.analyse = analyse
        
    def parse(self):

        """transformation method"""
        #switch to lower case
        self.analyse = self.analyse.lower()
        
        #remove accent
        self.analyse = ''.join((c for c in unicodedata.normalize('NFD', self.analyse) if unicodedata.category(c) != 'Mn'))
        
        #remove punctuation
        self.analyse = re.sub(r"[.!,;?\']", " ", self.analyse).split()
        
        #check stopword
        self.analyse = [x for x in self.analyse if x not in config.STOPWORDS]

        #to convert the list to string.
        self.analyse = ' '.join(self.analyse)

        return self.analyse

class GoogleApi:

    def __init__(self,userQuery):

        self.user_query = userQuery
        self.latitude = float
        self.longitude = float
        self.global_address = str


    def position(self):

        payload = {'address': self.user_query, 'key' : config.API_KEY}
        result = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
        google_maps = result.json()
        status = google_maps['status']
        if status == 'OK':
            self.latitude = google_maps['results'][0]['geometry']['location']['lat']
            self.longitude = google_maps['results'][0]['geometry']['location']['lng']
            self.global_address = google_maps['results'][0]['formatted_address']
            return self.latitude, self.longitude, self.global_address
        
        elif status =='ZERO_RESULTS':
            print("adresse non trouvée")

class WikiApi:

    def __init__(self,latitude, longitude):
        """ Initializer / Instance Attributes """
        self.latitude = latitude
        self.longitude = longitude

    def get_wiki(self):

        geo = '{}|{}'.format(self.latitude, self.longitude)
        payload = {'action': 'query',
                   'generator': 'geosearch',
                   'ggsradius':50, 
                    'ggscoord': geo, 
                    'prop': 'extracts',
                    'explaintext': True,
                    'exsentences': 2, 
                    'exlimit': 1,
                    'redirects': True, 
                    'format': 'json', 
                    'formatversion': 2}

        response = requests.get('https://fr.wikipedia.org/w/api.php', params=payload)
        media_wiki = response.json()
        try:
            # Return the first two sentences of the intro in the extracts,
            # in plain text, of the place with that coordinates (see payload).
            first_2_sentences = media_wiki['query']['pages'][0]['extract']
            pageid = media_wiki['query']['pages'][0]['pageid']
            return first_2_sentences, pageid
        except KeyError:
            pass