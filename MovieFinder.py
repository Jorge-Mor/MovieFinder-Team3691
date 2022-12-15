"""
Course: CST 205
Title: Movie Finder
Abstract: In terms of the future of this project we want to be able to display more information about the movies we are displaying.
We also wanted to get a second part of the website where the user can "save" these images and later manipulate them as they please.
Our last idea was to show not just once movie when a movie is searched but everyone movie that shares a similar name in case the user does not exactly know the name of the movie they are looking for
Authors:Anitha Rajamohan, Jorge Mereno, Kyle Borch
Date: 12/14/2022
Sources cited: https://www.themoviedb.org/documentation/api
Work Distribution: Anitha Rajamohan and Jorge Mereno find the Api for the project
Anitha Rajamohan: # index Api call and design
                  # movieTitle(title) funtion and moreInfo page Styling and displaying data
Jorge Mereno: # activated the serch button and rendered data to index2 page
              # funtion worked on Playlist(FlaskForm), themoviedbAPI(movie), store_song(movie), index(),movie()
Kyle Borch: worked on index2 Styling and displaying data in /movie page
"""
import requests, json
from pprint import pprint
from flask import Flask,render_template, flash, redirect
from flask_bootstrap import Bootstrap5
import random
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# create an instance of Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'

#Create Bootstrap object (after Flask object):
bootstrap = Bootstrap5(app)

#class for playlist
# worked by Jorge Mereno
class Playlist(FlaskForm):
  song_title = StringField(
    'Movie Title', 
    validators=[DataRequired()]
  )

#geting Api call
# worked by Jorge Mereno
def themoviedbAPI(movie):
  my_key = '933dcbef063eeaeab80f38d6e792311c'
  apiLink = 'https://api.themoviedb.org/3/search/movie?api_key='+my_key+'&query='+movie


  try:
    r = requests.get(apiLink)
    data = r.json()

  except:
    print('please try again')
  return data

#Assigning movie names to background to get random colors and image on the home screen
# worked by Jorge Mereno
movieNames = ['avenger', 'thing', 'black', 'wave', 'it', 'teen', 'john', 'the', 'him', 'one', 'hero']
background =['secondary', 'success','warning','info','primary','danger']
movieInformation = []

# worked by Jorge Mereno
def store_song(movie):
  movieI = themoviedbAPI(movie)
  movieInformation.append(movieI)

#home page
# worked by Jorge Mereno, color added by Anitha Rajamohan
@app.route('/', methods=('GET', 'POST'))
def index():
  #Collecting info from the home page and rendering to a new page if the search button is clicked
  form = Playlist()
  if form.validate_on_submit():
    movieInformation = []
    store_song(form.song_title.data)
    return redirect('/movie')

  data=themoviedbAPI(random.choice(movieNames))
  random_number = random.randint(0, 6)
  random_color = random.randint(0, 5)
  return render_template('index.html', form=form, my_data=data,random_number=random_number,background=background,random_color=random_color)

#movie page
# by Jorge Mereno
@app.route('/movie')
def movie():
  return render_template('index2.html', movieInfo=movieInformation)

# movie page by title gived more information about movie
# added by Anitha Rajamohan
@app.route('/movie/<title>')
def movieTitle(title):
  random_color = random.randint(0, 5)
  data=themoviedbAPI(title)
  return render_template('moreInfo.html', movieInfo=data,background=background,random_color=random_color)



