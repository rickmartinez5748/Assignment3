import urllib.request
import json

def get_iss_coordinates():
   
   url="http://api.open-notify.org/iss-now.json"
   request=urllib.request.urlopen(url)
   result=json.loads(request.read())
   
   lat=result["iss_position"]["latitude"]
   lon=result["iss_position"]["longitude"]

   return lat, lon

position=get_iss_coordinates()   
print(f"The current position (longitude, latitude) of the International Space Shuttle is: ({position[0]}, {position[1]})")
