import requests, json
from pprint import pprint
from flask import Flask

# create an instance of Flask
app = Flask(__name__)

def getTitle():
    title = input("Please enter a title for the movie and make sure to input it corrctly: ")
    return title


my_key = 'bcc4d5b1'
apiLink = ' http://www.omdbapi.com/?s=' + getTitle() + '&apikey=bcc4d5b1'

try:
  r = requests.get(apiLink)
  data = r.json()
  pprint(data)
except:
  print('please try again')

posterLinks = []
for movie in data['Search']:
    # print(movie['Title'], movie['Year'])
    posterLinks.append(movie['Poster'])
pprint(posterLinks)

# route decorator binds a function to a URL
@app.route('/')
def hello():
   return 'Hello world from Flask!'