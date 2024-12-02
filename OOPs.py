"""Write OOP classes to handle the following scenarios:

- A user can create and view 2D coordinates
- A user can find out the distance between 2 coordinates
- A user can find find the distance of a coordinate from origin
- A user can check if a point lies on a given line
- A user can find the distance between a given 2D point and a given line"""
print("OOP Program 1")

class Point:
    
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<{},{}>'.format(self.x, self.y)

    def euc_dis(self, other):
    # self is the first object and other is the other object for class Point
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5
        # Can also write as --> return self.euclidean_distance(Point(0,0))

class Line:

  def __init__(self,A,B,C):
    self.A = A
    self.B = B
    self.C = C

  def __str__(self):
    return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)
  
  def point_on_line(line,point):
    if line.A*point.x + line.B*point.y + line.C == 0:
      return "lies on the line"
    else:
      return "does not lie on the line"

  def shortest_distance(line,point):
    return abs(line.A*point.x + line.B*point.y + line.C)/(line.A**2 + line.B**2)**0.5
    
P1 = Point(2,5)
P2 = Point(3,8)
print(f"The distance between point{P1} and {P2} is, ", P1.euc_dis(P2))
L1 = Line(1,2,3)
print(L1.point_on_line(P1))
print(L1.point_on_line(P2))

## How objects access attributes

class Person:

    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == 'india':
            print('Namaste',self.name)
        else:
            print('Hello',self.name)

# how to access attributes
p = Person('nitish','india')
print(p.name)
print(p.country)
p.greet()

# what if i try to access non-existent attributes
p.gender