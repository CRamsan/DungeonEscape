import string
import random
import math

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class Vector():
        
        def __init__(self, x=0, y=0):
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

        def __eq__(self, obj):
            return self.x == obj.x and self.y == obj.y
        
        def __ne__(self, obj):
            return self.x != obj.X or self.y != obj.y
        
        def __str__(self):
            return str(self.x) + ", " + str(self.y)
            
def Polygon():
    
    def __init__(self, x, y):
        self.points = []
        self.edges = []
            
    def build_edges(self):
        self.edges[:] = []
        for i in range(len(self.points)):
            p1 = self.points[i]
            if i + 1 >= len(self.points):
                p2 = self.points[0]
            else:
                p2 = self.points[i + 1]
            self.edges.append(p2 - p1);


    def center(self):
        totalx = 0
        totaly = 0
        for point in self.points:
            totalx += point.x;
            totaly += point.y;

        return Vector(totalx / len(self.points), totaly / len(self.points));


    def offset(self, x, y):
        for point in self.points:
            point = Vector(point.x + x, point.y + y);



    def __str__ (self):
        result = ''
        for point in self.points:
            if result != "":
                result += " "
            result += "{" + str(point) + "}"
        return result;


def Collision():

        def polygon_collision(self, polygonA, polygonB, velocity):


            Intersect = True
            WillIntersect = True

            edgeCountA = len(polygonA.edges)
            edgeCountB = len(polygonB.edges)
            minIntervalDistance = float("inf")
            translationAxis = Vector()

            for edgeIndex in range(edgeCountA + edgeCountB):
                if edgeIndex < edgeCountA:
                    edge = polygonA.edges[edgeIndex]
                else:
                    edge = polygonB.edges[edgeIndex - edgeCountA]
        

                axis = Vector(-edge.Y, edge.X)
                axis.normalize()
                
                resA = self.project_polygon(axis, polygonA)
                resB = self.project_polygon(axis, polygonB)

                minA = resA[0]
                minB = resA[1]
                maxA = resB[0]
                maxB = resB[1]

                if (self.interval_distance(minA, maxA, minB, maxB) > 0) :
                    Intersect = False

                velocityProjection = axis.dot_product(velocity);

                if velocityProjection < 0:
                    minA += velocityProjection
                else:
                    maxA += velocityProjection
        

                intervalDistance = self.interval_distance(minA, maxA, minB, maxB);
                if intervalDistance > 0:
                    WillIntersect = False

                if not Intersect and not WillIntersect:
                    break


                intervalDistance = math.fabs(intervalDistance)
                if intervalDistance < minIntervalDistance:        
                    minIntervalDistance = intervalDistance
                    translationAxis = axis
                    
                    d = polygonA.center() - polygonB.center()
                    if d.dot_product(translationAxis) < 0:
                        translationAxis = -translationAxis
            
            if WillIntersect:
                MinimumTranslationVector = translationAxis * minIntervalDistance

            return WillIntersect, Intersect, MinimumTranslationVector


        def interval_distance(self, minA, maxA, minB, maxB):
            if minA < minB:
                return minB - maxA;
            else:
                return minA - maxB;
    
        def project_polygon(self, axis, polygon):

            d = axis.dot_product(polygon.points[0])
            minP = d
            maxP = d
            for i in range(len(polygon.points)):
                d = polygon.points[i].dot_product(axis);
                if d < minP:        
                    minP = d
                else:
                    if d > maxP:
                        maxP = d;
            return minP, maxP
            
        
    


