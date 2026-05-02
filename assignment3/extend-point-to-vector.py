#task5 
import math

class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equality(self, other_point):
        if (other_point.x == self.x) and (other_point.y == self.y): 
            return True 
        
        return False

    def string_represent(self):
        return f"This Point contains the x value {self.x} and the y value {self.y}"

    def euclidian_dist(self, other_point):
        x_s = (other_point.x - self.x) ** 2
        y_s = (other_point.y - self.y) ** 2
        x_plus_y = x_s + y_s
        return math.sqrt(x_plus_y)


class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def string_represent(self):
        return f"Vector has x value of {self.x} and y value of {self.y}"
    
    def __add__(self, other_vector):
        new_x = other_vector.x + self.x
        new_y = other_vector.y + self.y
        return Vector(new_x, new_y)
    
point1 = Point(1, 2)
point2 = Point(10, 20)
point3 = Point(1, 2)
point4 = Point(0, 0)
point5 = Point(0, 0)

print(point1.euclidian_dist(point2))
print(point4.euclidian_dist(point5))
print(point1.string_represent()) #should be 1 and 2
print(point1.equality(point3))

vector1 = Vector(100, 200)
vector2 = Vector(300, 400)
print(vector1.string_represent()) #should be 100 and 200
print((vector1 + vector2).string_represent()) #should be 400 and 600
    

    

    