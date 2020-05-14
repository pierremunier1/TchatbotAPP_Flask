from tchatbotapp import tchatbotapp

elif os.environ.get('ENV') == 'PRODUCTION':
    DEBUG = False 
   else:
        DEBUG = True

if __name__ == "__main__":
   tchatbotapp.run(debug=DEBUG)
   
    
    