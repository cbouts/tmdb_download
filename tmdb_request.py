# print("hello")
import urllib.request
import json
import sys
import os

api_key = sys.argv[1]

if not os.path.exists('json_files'):
	os.mkdir('json_files')

# response = urllib.request.urlopen('https://api.themoviedb.org/3/movie/latest?api_key=' + api_key)
# json_response = json.load(response)
# movie_count = int(json_response['id'])
# print (movie_count)

# movie_start = movie_count-5
movie_id = '550'
# how to do a for loop in order to get info on last 5 movies
response = urllib.request.urlopen('https://api.themoviedb.org/3/movie/' + movie_id +'?api_key=' + api_key)
json_response = json.load(response)
print(json_response)
