import requests, json
from pprint import pprint
from flask import Flask,render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)

#Create Bootstrap object (after Flask object):
bootstrap = Bootstrap5(app)

def getTitle():
    title = input("Please enter a title for the movie and make sure to input it corrctly: ")
    return title

#api call return the posterLinks
def callApi():
  my_key = 'bcc4d5b1'
  apiLink = ' http://www.omdbapi.com/?s=' + getTitle() + '&apikey=bcc4d5b1'

  try:
    r = requests.get(apiLink)
    data = r.json()
    # pprint(data)
  except:
    print('please try again')

  posterLinks = []
  for movie in data['Search']:
      # print(movie['Title'], movie['Year'])
      posterLinks.append(movie['Poster'])

  return posterLinks

# route decorator binds a function to a URL
@app.route('/')
def hello():
  return render_template('index.html')

# pprint(callApi())