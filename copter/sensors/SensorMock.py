from shapely import affinity
from shapely.geometry import LineString, Point, MultiPoint, GeometryCollection, MultiLineString
from shapely.ops import cascaded_union

from copter.sensors.Sensor import Sensor
from geometry.Circle import Circle
from geometry.PointVector import PointVector

__author__ = 'Martin'


class SensorMock(Sensor):
    def __init__(self, sensor_range, obstacles, other_copters):
        self.sensor_range = sensor_range
        self.sweep_resolution = 25
        self.obstacles = obstacles
        self.other_copters = other_copters

    def collect_obstacles_closest_points(self, copter_position):
        obstacle_entities = list(map(
            lambda obstacle: obstacle.geometric_entity.get_lib_conversion(),
            self.obstacles))
        return self.get_closest_points(copter_position, obstacle_entities)

    def collect_other_copters_closest_points(self, position):
        other_copters_circles = list(map(
            lambda copter: Circle(PointVector(copter.position.x, copter.position.y), copter.size).get_lib_conversion(),
            self.other_copters))
        return self.get_closest_points(position, other_copters_circles)

    # inspired by http://gis.stackexchange.com/q/81613
    def get_closest_points(self, copter_position, entities):
        position = copter_position.get_lib_conversion()
        all_entities = cascaded_union(entities)

        starting_sweep_line = LineString(
            [position, (position.x, position.y - self.sensor_range)])
        sweep_lines = [affinity.rotate(starting_sweep_line, i, position)
                       for i in range(0, 360, self.sweep_resolution)]
        radial_sweep = cascaded_union(sweep_lines)

        perimeter = []
        for radial_line in radial_sweep:
            intersection = radial_line.intersection(all_entities)

            if isinstance(intersection, Point):
                perimeter.append(intersection)
            elif isinstance(intersection.type, MultiPoint):
                intersection_dict = {}
                for intersection_point in intersection:
                    intersection_dict[position.distance(intersection_point)] = intersection_point
                # add closest intersection point
                perimeter.append(intersection_dict[min(intersection_dict.keys())])
            elif isinstance(intersection, LineString):
                closest_point = self.get_line_closest_point(position, intersection)
                perimeter.append(closest_point)
            elif isinstance(intersection, MultiLineString):
                for line in intersection:
                    closest_point = self.get_line_closest_point(position, line)
                    perimeter.append(closest_point)
            elif isinstance(intersection, GeometryCollection):
                pass
            else:
                raise ValueError("Unknown type {}".format(intersection.__class__.__name__))

        return list(map(lambda p: PointVector(p.x, p.y), perimeter))

    @staticmethod
    def get_line_closest_point(position, line):
        p1 = Point(line.coords[0][0], line.coords[0][1])
        p2 = Point(line.coords[1][0], line.coords[1][1])
        if position.distance(p1) < position.distance(p2):
            return p1
        else:
            return p2
