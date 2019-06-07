#!/usr/bin/env python

__author__ = '???'

import requests
import json
import time
import turtle
import urllib2


def current_astros():
    """list total number of astronauts as well as their names"""

    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()

    print("There are currently {} people in space".format(data["number"]))
    for i in data["people"]:
        print("{} is on the {}".format(i["name"], i["craft"]))


def current_location_iss():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()

    timestamp = data['timestamp']
    lat = data["iss_position"]["latitude"]
    long = data["iss_position"]["longitude"]

    
    print("The ISS is currently located at latitude: {} and longitude: {} at this time: {}"\
        .format(data["iss_position"]["latitude"], data["iss_position"]["longitude"], timestamp))

    return lat, long, timestamp


def world_map(lat, long):
    """Setting up canvas for turtle"""

    world_map = turtle.Screen()
    world_map.setup(720, 360)
    world_map.bgpic('map.gif')
    world_map.setworldcoordinates(-180, -90, 180, 90)
    world_map.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(float(long), float(lat))

    """checking when iss will pass over"""

    indy_lat = 39.7684
    indy_long = -86.1581
    url = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}'.format(
        indy_lat, indy_long)
    response = urllib2.urlopen(url)
    result = json.loads(response.read())
    response.close()
    passover_time = result['response'][0]['risetime']

    """adding indy location to map"""

    indy = turtle.Turtle()
    indy.penup()
    indy.goto(indy_long, indy_lat)
    indy.dot(7, 'yellow')
    indy.hideturtle()
    indy.color('yellow')
    indy.write(time.ctime(passover_time))





def main():
    current_astros()
    coordinates = current_location_iss()
    world_map(coordinates[0], coordinates[1])
    turtle.exitonclick()



if __name__ == '__main__':
    main()
