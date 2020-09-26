# print("hello")
import urllib.request
import json
import sys
import os
import time

api_key = sys.argv[1]
# feeds the api key into api key
# sys.argv when you're running the program instead of doing python tmdb_request.py, you type in the whole api key after tmdb_request.py


if not os.path.exists('json_files'):
	os.mkdir('json_files')
	# catch is that if the file has already been made, you don't want to make it again, so you have the if statement.

response = urllib.request.urlopen('http://api.themoviedb.org/3/movie/latest?api_key=' + api_key)
json_response = json.load(response)
movie_count = int(json_response['id'])
# print (movie_count)

# now that we've gotten a movie count, the next step is to get all the info from the db.

movie_start = movie_count-30
# so we want to download the most recent 30 movies. use the - to indicate that you're counting from the end.

# we get one movie first, and then do a for loop to get all the info from the site.

for i in range(movie_start,movie_count):
	print(i)
	# ususally the first line in for loops is print. it will tell you how many i's the program has already processed.
	movie_id = str(i)

	# how to do a for loop in order to get info on the most recent 5 movies
	response = urllib.request.urlopen('http://api.themoviedb.org/3/movie/' + movie_id +'?api_key=' + api_key)
	# bc we want a json response, 
	json_response = json.load(response)
	# print(json_response)
	# to write json_response into folder, we need to open the file first.
	# use 
	f = open("json_files/tmdb" + movie_id + ".json", "w")
	# this is for opening a file. usually you need to specify what you're doing. "w" means writing
	f.write(json.dumps(json_response))
	# json dumps puts things into a file. 
	f.close()
	time.sleep(15)
	# sleep so that it doesn't think you're hacking the site


