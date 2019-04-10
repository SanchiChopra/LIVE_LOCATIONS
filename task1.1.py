import json
import turtle
import urllib.request
import time

# Don't need to make a tkinter window
# tutle.Screen create the output
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print('people in space', result['number'])
people = result['people']
for p in people:
  print(p['name'])

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result=json.loads(response.read())
print(result)

location=result['iss_position']
# Convert the lat and lon to float
# Currently it's a string
lat=float(location['latitude'])
lon=float(location['longitude'])
print('Latitude:',lat)
print('Longitude:',lon)


# Creating output Screen
# screen <- Screen object
screen=turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.png')
# Can set shape to a gif image file
# Or use a preset shape like ["square", "triangle", "turtle" ...]
screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))

# iss is the current location of iss
iss=turtle.Turtle()
iss.shape("turtle")
iss.setheading(90)
iss.penup()
iss.goto(lon,lat)

lat=29.5502
lon=-95.097
# location is some random location
# (29.5502, -95.097)
location=turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

# This location should use the iss lat and lon coordinates
# Not the random ones and shoud display over iss object
url='http://api.open-notify.org/iss-pass.json'
url=url+'?lat='+str(lat)+'&lon='+str(lon)
response=urllib.request.urlopen(url)
result=json.loads(response.read())
over=result['response'][1]['risetime']
#print(over)
style=('Arial',6,'bold')
location.write(time.ctime(over),font=style)

# Display the screen and wait for use to click on it to exit
screen.exitonclick()
