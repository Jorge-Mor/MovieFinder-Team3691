import requests, json
from pprint import pprint
from flask import Flask,render_template
from flask_bootstrap import Bootstrap5
import random

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
  return data


def posterLinks(data):
  posterLinks = []
  for movie in data['Search']:
      # print(movie['Title'], movie['Year'])
      posterLinks.append(movie['Poster'])

  return posterLinks

# https://api.themoviedb.org/3/search/movie?api_key=933dcbef063eeaeab80f38d6e792311c&query=Life
def themoviedbAPI():
  my_key = '933dcbef063eeaeab80f38d6e792311c'
  apiLink = 'https://api.themoviedb.org/3/search/movie?api_key='+my_key+'&query=Life'

  try:
    r = requests.get(apiLink)
    data = r.json()
    pprint(data)
  except:
    print('please try again')
  return data


# route decorator binds a function to a URL
@app.route('/')
def hello():
  data=themoviedbAPI()
  random_number = random.randint(0, 10)
  pprint(data)
  return render_template('index.html',my_data=data,random_number=random_number)

# pprint(posterLinks(callApi()))