import requests, json
from pprint import pprint

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
print(posterLinks)
