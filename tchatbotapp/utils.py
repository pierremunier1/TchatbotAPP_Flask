import re
import config
import unicodedata



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
        
        