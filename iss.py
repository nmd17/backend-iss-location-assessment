#!/usr/bin/env python

__author__ = '???'

import requests
import json
import turtle


def current_astros():
    """list total number of astronauts as well as their names"""

    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()

    print("There are currently {} people in space".format(data["number"]))
    for i in data["people"]:
        print("{} is on the {}".format(i["name"], i["craft"]))

current_astros()

def current_location_iss():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    
    print("The ISS is currently located at latitude: {} and longitude: {}"\
        .format(data["iss_position"]["latitude"], data["iss_position"]["longitude"]))

current_location_iss()

def world_map():
    screen = turtle.Screen()
    iss = turtle.Turtle()
    screen.bgpic("map.gif")
    screen.update()

world_map()





def main():
    pass


if __name__ == '__main__':
    main()
