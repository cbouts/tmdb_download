# print("hello")
import urllib.request
import json

response = urllib.request.urlopen('https://api.themoviedb.org/3/movie/550?api_key=a2e0b327cacf1f08847bb4fea510af55')
json_response = json.load(response)
print (json_response)