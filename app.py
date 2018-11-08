from flask import Flask, jsonify
from geopy.distance import Point, VincentyDistance
import math
app = Flask(__name__)

@app.route('/')
def index():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        a friendly welcome page
    """
    return "<h1>Welcome to Pointdexter!</h1>"

@app.route('/pointdexter/api/v1/points/<float:lat>/<float:lon>/scatter/<float:distance>/<int:width>/<int:height>', methods=['GET'])
def scatter_points(lat, lon, distance, width, height):
    """
    This function calculates every coordinates in the 
    width x height grid of equally distribuited points.

    :param float lat: Latitude for the starting point
    :param float lon: Longitude for the starting point
    :param float distance: Radius of the circle in km
    :param int width: Number of points from West to East
    :param int height: Number of points from North to South
    :return:        JSON {scatteredPoints{lat, lon}, size}
    """
    scattered_points = []
    first_column = get_first_column(lat, lon, distance, height)
    for point in first_column:
        scattered_points.append(point)
        this_lat, this_lon = point['lat'], point['lon']
        for w in range(width - 1):
            next_lat, next_lon = get_next_point(this_lat, this_lon, distance, 90)
            scattered_points.append({'lat': next_lat, 'lon': next_lon})
            this_lat, this_lon = next_lat, next_lon
    return jsonify({'scatteredPoints': scattered_points, 'size': len(scattered_points)})

def get_first_column(lat, lon, distance, height):
    """
    This function calculates the first column of height
    points. Points lie in a zig-zag line. Every two 
    subsequent points are at distance*math.sqrt(2) km.

    :param float lat: Latitude of the first point
    :param float lon: Longitude of the first point
    :param float distance: Radius of the circle in km
    :param int height: Number of points in the first column
    """
    points = [{'lat': lat, 'lon': lon}]
    this_lat, this_lon = lat, lon
    for h in range(height-1):
        if h % 2 == 0:
            bearing = 135
        else:
            bearing = 225
        next_lat, next_lon = get_next_point(this_lat, this_lon, distance*math.sqrt(2), bearing)
        points.append({'lat': next_lat, 'lon': next_lon})
        this_lat, this_lon = next_lat, next_lon
    return points

def get_next_point(lat, lon, distance, bearing):
    """
    This function calculates the next point given an 
    origin point, a distance and a bearing.

    :param float lat: Latitude of the first point
    :param float lon: Longitude of the first point
    :param float distance: Radius of the circle in km
    :param float bearing: Bearing angle in degrees
    """
    origin = Point(lat, lon)
    destination = VincentyDistance(kilometers=distance).destination(origin, bearing)
    return destination.latitude, destination.longitude

if __name__ == '__main__':
    app.run()
