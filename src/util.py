import string
import random
import math

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class Vector():
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.mag = self.magnitude
            
        def magnitude(self):
            return math.sqrt(self.x * self.x + self.y * self.y)
        

        def normalize(self):
            self.mag = self.magnitude
            self.x = self.x / self.mag
            self.y = self.y / self.mag

        def clone_normalized(self):
            return Vector(self.x / self.magnitude(), self.y / self.magnitude());

        def dot_product(self, vector):
            return self.x * vector.x + self.y * vector.y

        def distance_to(self, vector):
            return math.sqrt(math.pow(vector.x - self.x, 2) + math.pow(vector.y - self.y, 2))

        def __add__(self, vector_a, vector_b):
            return Vector(vector_a.x + vector_b.x, vector_a.y + vector_b.y);

        def __sub__(self, vector_a, vector_b):
            return Vector(vector_a.x - vector_b.x, vector_a.y - vector_b.y);

        def __mul__(self, vector_a, multiplier):
            return Vector(vector_a.x * multiplier, vector_a.y * multiplier);

        def equals(self, obj):
            return self.x == obj.x and self.y == obj.y

