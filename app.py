import requests
import math
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="app")


def get_dist(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b
    return math.hypot(x1-x2, y1-y2)

accesskey="pk.eyJ1Ijoic2hhaGFyeWFya2hhbiIsImEiOiJjbDNsYzJudHAwY3duM2ttOGFiYnNyaGRtIn0.CgVK7MGWS5B6McNa79F3nQ"
lasturl = "?alternatives=true&geometries=geojson&language=en&overview=simplified&steps=true&access_token="
p = print
source = ["-73.99118062955347","40.72995988399356"]  #testsource
destination = ["-73.996698329012", "40.725466695131644"] #testdestination
R = 6373.0 #Approximate radius of Earth in kms
while(True):
    location1 = geolocator.geocode(input("Please enter Source: "))
    location2 = geolocator.geocode(input("Please enter Destination: "))
    if location1 == None or location2 == None:
        p("Please enter a valid location!")
    else:
        break

source[0] = str(location1.longitude)
source[1] = str(location1.latitude)

destination[0] = str(location2.longitude)
destination[1]  = str(location2.latitude)

p(f"Source: {source} Destination:{destination}")

markingDict = {
    ',' :"%2C",
    ';'  :"%3B"
}
baseurl = "https://api.mapbox.com/directions/v5/mapbox/driving/"

fullurl = f"{baseurl}{source[0]}{markingDict[',']}{source[1]}{markingDict[';']}{destination[0]}{markingDict[',']}{destination[1]}{lasturl}{accesskey}" 

r = requests.get(url = fullurl)
distlist = {}
distances = []
data = r.json()
numOfRoutes  = len(data['routes'])
p(f"Number of Routes: {numOfRoutes}")
for id in range(numOfRoutes):
    distance = 0
    route = data['routes'][id]["geometry"]["coordinates"]
    for x in range(len(route) - 1):
        a = (route[x][0],route[x][1])
        b = (route[x+1][0],route[x+1][1])
        distance += get_dist(a, b)
    distlist[id] = distance
    distances.append(distance)

p(f"Distances of All Routes to Destination: {distlist}")
routeid = distances.index(min(distances))
p(f"Route ID: {routeid} Distance of Minimal Route: {min(distances)}")
#print(data['routes'][routeid]["geometry"]["coordinates"])
dictt = {}
dictt["Route"] = data['routes'][routeid]["geometry"]["coordinates"]
p(f"Selected Route {dictt}")


