#!/usr/bin/env python

"""A command-line tool for geospatial calculations."""
import click
from mylib.geotools import get_most_populated_cities, get_distance


@click.group()
def cli():
    pass


@cli.command("distance")
@click.argument("city1", type=str, default="New York")
@click.argument("city2", type=str, default="Los Angeles")
def distance_cli(city1, city2):
    """Calculate the distance between two cities.
    Example:
    $ ./geocli distance "New York" "Los Angeles"

    """
    # get the distance between the two cities
    dist = get_distance(city1, city2)
    # print the distance using different colors for cities and distance
    click.secho(
        click.style(city1, fg="green")
        + " and "
        + click.style(city2, fg="green")
        + " are "
        + click.style(f"{dist:.2f} miles", fg="blue")
        + " apart."
    )


@cli.command("cities")
def cities_cli():
    """List the 10 most populated cities in the USA."""
    # get the list of cities
    cities = get_most_populated_cities()
    # print the cities using different colors
    click.secho("The 10 most populated cities in the USA are:", fg="green")
    for city in cities:
        click.secho(" - " + city, fg="blue")


if __name__ == "__main__":
    cli()
