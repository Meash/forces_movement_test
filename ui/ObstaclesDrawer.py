from copter.util.ObstacleListener import ObstacleListener
from geometry.PointHelper import PointHelper

__author__ = 'Martin'


class ObstaclesDrawer(ObstacleListener):
    def __init__(self, copter, canvas):
        self.copter = copter
        self.canvas = canvas
        self.point_helper = PointHelper(canvas)
        self.drawn_obstacles = []
        self.drawn_connectors = []

    def on_obstacles_update(self, obstacle_closest_points):
        drawn_obstacles = list(self.drawn_obstacles)
        drawn_connectors = list(self.drawn_connectors)
        self.draw_obstacles(obstacle_closest_points)
        for drawn_connector in drawn_connectors:
            self.canvas.delete(drawn_connector)
            self.drawn_connectors.remove(drawn_connector)
        for drawn_obstacle in drawn_obstacles:
            self.canvas.delete(drawn_obstacle)
            self.drawn_obstacles.remove(drawn_obstacle)

    def draw_obstacles(self, obstacle_closest_points):
        obstacle_size = 5 / 2

        copter_x = self.copter.position.x
        copter_y = self.copter.position.y
        copter_y = self.point_helper.invert_y(copter_y)

        for obstacle_point in obstacle_closest_points:
            x = obstacle_point.x
            y = obstacle_point.y
            y = self.point_helper.invert_y(y)
            drawn_obstacle = self.canvas.create_oval(
                x - obstacle_size, y - obstacle_size,
                x + obstacle_size, y + obstacle_size,
                fill="red"
            )
            self.drawn_obstacles.append(drawn_obstacle)

            drawn_connector = self.canvas.create_line(
                x, y, copter_x, copter_y,
                fill="darkgray"
            )
            self.drawn_connectors.append(drawn_connector)
