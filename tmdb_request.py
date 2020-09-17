# print("hello")
import urllib.request
import json
import sys

api_key = sys.argv[1]

response = urllib.request.urlopen('https://api.themoviedb.org/3/movie/latest?api_key=' + api_key)
json_response = json.load(response)
movie_count = int(json_response['id'])
print (movie_count)


# should in