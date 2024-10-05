""" Build a library of geospacial tools. """

from geopy import distance
import geopy

USER_AGENT = "python-for-devops"

# create a function that returns a list of the 10 most populated cities in the USA
def get_most_populated_cities():
    """Return a list of the 10 most populated cities in the USA."""
    cities = [
        "New York",
        "Los Angeles",
        "Chicago",
        "Houston",
        "Phoenix",
        "Philadelphia",
        "San Antonio",
        "San Diego",
        "Dallas",
        "San Jose",
    ]
    return cities


# cretae a function that returns the distance between two cities
def get_distance(city1, city2):
    """Return the distance between two cities."""
    geolocator = geopy.Nominatim(user_agent=USER_AGENT)
    location1 = geolocator.geocode(city1)
    location2 = geolocator.geocode(city2)
    return distance.distance(location1.point, location2.point).miles
