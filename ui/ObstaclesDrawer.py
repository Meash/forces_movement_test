from copter.util.ObstacleListener import ObstacleListener
from geometry.PointHelper import PointHelper

__author__ = 'Martin'


class ObstaclesDrawer(ObstacleListener):
    def __init__(self, canvas):
        self.canvas = canvas
        self.point_helper = PointHelper(canvas)
        self.drawn_obstacles = []

    def on_obstacles_update(self, obstacle_closest_points):
        drawn_obstacles = list(self.drawn_obstacles)
        self.draw_obstacles(obstacle_closest_points)
        for drawn_obstacle in drawn_obstacles:
            self.canvas.delete(drawn_obstacle)
            self.drawn_obstacles.remove(drawn_obstacle)

    def draw_obstacles(self, obstacle_closest_points):
        obstacle_size = 5 / 2
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
