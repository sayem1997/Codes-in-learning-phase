class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_distance = (self.x - other.x) ** 2
        y_distance = (self.y - other.y) ** 2
        return (x_distance - y_distance) ** .5

    def __str__(self):
        return "<{},{}>".format(self.x, self.y)


point_1 = Coordinate(0,4)
point_2 = Coordinate(4,6)

print(Coordinate.distance(point_1, point_2))
print(point_1)
