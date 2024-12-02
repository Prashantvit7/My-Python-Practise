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
# Note p is not object but contains address of the object
print(p.name)
print(p.country)
p.greet()

# what if i try to access non-existent attributes
p.gender # It gives AttributeError: 'Person' object has no attribute 'gender'

""""Reference Variables
Reference variables hold the objects SO IT BASICALLY HOLDS THE MEMORY LOCATION OF OBJECT
We can create objects without reference variable as well
An object can have multiple reference variables
Assigning a new reference variable to an existing object does not create a new object"""


class Person:

  def __init__(self):
    self.name = 'nitish'
    self.gender = 'male'

p = Person() # p is not an Object but it is a reference variable which points to memeory address of object
q = p # q and p are pointing to the same memory location

print(p.name)
print(q.name)
q.name = 'ankit'
print(q.name)
print(p.name) # Since p and q are pointing to same object once we change value it is changed for both.



#Pass by reference
# In python we can pass object as input to a function
# Also a function in return can provide object of a class
# All objects in Python are mutable by default provided in memory changes happenned.
class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

# outside the class -> function
def greet(person):
  print('Hi my name is',person.name,'and I am a',person.gender)
  p1 = Person('ankit','male')
  return p1

p = Person('nitish','male')
x = greet(p)
print(x.name)
print(x.gender)


############################### ENCAPUSULATION ###############################

# instance var -> pythontutor.com
class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input # name and country are attributes 
    self.country = country_input
    # Instance variables are those variables whose value is different for different objects
    # eg for name as iv for two objects p1 and p2 values are different

p1 = Person('nitish','india')
p2 = Person('steve','australia')


class Atm:

  # constructor(special function)->superpower -> 
  def __init__(self):
    print(id(self))
    self.pin = ''
    self.__balance = 0
    #self.menu()

  def get_balance(self):
    return self.__balance

  def set_balance(self,new_value):
    if type(new_value) == int:
      self.__balance = new_value
    else:
      print('beta bahot maarenge')

  def __menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()

  def create_pin(self):
    user_pin = input('enter your pin')
    self.pin = user_pin

    user_balance = int(input('enter balance'))
    self.__balance = user_balance

    print('pin created successfully')

  def change_pin(self):
    old_pin = input('enter old pin')

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input('enter new pin')
      self.pin = new_pin
      print('pin change successful')
    else:
      print('nai karne de sakta re baba')

  def check_balance(self):
    user_pin = input('enter your pin')
    if user_pin == self.pin:
      print('your balance is ',self.__balance)
    else:
      print('chal nikal yahan se')

  def withdraw(self):
    user_pin = input('enter the pin')
    if user_pin == self.pin:
      # allow to withdraw
      amount = int(input('enter the amount'))
      if amount <= self.__balance:
        self.__balance = self.__balance - amount
        print('withdrawl successful.balance is',self.__balance)
      else:
        print('abe garib')
    else:
      print('sale chor')

#Summary
# To avoid accendental changes to varibles make them private by adding __ in start, 
# similarly methods can also be made pvt..
# It is a good practise to make all variables as private

########################################### list of objects

# We can create multiple objects and make them as list/Tuple/Dict
class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

p1 = Person('nitish','male')
p2 = Person('ankit','male')
p3 = Person('ankita','female')

L = [p1,p2,p3]

for i in L:
  print(i.name,i.gender)



#################################################Static Variables(Vs Instance variables)

# Need : Using Instance variable you cannot have a counter variable
# Just as Instance variable is of object, static varible is of class.
# Instance varible is different for every object, and value of static varible is same for all objects

"""In Python, the key difference between instance variables and static variables (also known as class variables) lies in their scope and association:
Instance Variables:
Scope: Belong to a specific instance of a class.
Association: Each instance of the class has its own copy of the instance variable, allowing different objects to hold different values for the same variable.
Definition: Declared within the class's methods, typically within the constructor (__init__), using the self keyword.
Access: Accessed using the instance object (self.variable_name).
Example:
Python


Execution output
class Car:
    def __init__(self, color):
        self.color = color  # Instance variable

red_car = Car("red")
blue_car = Car("blue")

print(red_car.color)
print(blue_car.color)
red
blue
Static Variables (Class Variables):
Scope: Belong to the class itself, shared across all instances.
Association: All instances of the class share the same value for the static variable.
Definition: Declared directly within the class, outside of any method.
Access: Accessed using the class name (ClassName.variable_name) or through an instance (instance.variable_name).
Example:
Python


Execution output
class Car:
    wheels = 4  # Static variable

    def __init__(self, color):
        self.color = color  # Instance variable

red_car = Car("red")
blue_car = Car("blue")

print(Car.wheels)
print(red_car.wheels)
print(blue_car.wheels)
4
4
4
Key Points:
Use instance variables for data that is unique to each object.
Use static variables for data shared across all instances of the class.
Static variables can be accessed through both the class and its instances, while instance variables can only be accessed through the instance."""

# Instance varible is defined inside __init__....So self. used for IV eg self.x
# Static varible is inside class, outside of all methods. eg <clas_name>.x
# To access static methods you don't need to create object and can be accessed via classname

class Atm:

  __counter = 1

  # constructor(special function)->superpower -> 
  def __init__(self):
    print(id(self))
    self.pin = ''
    self.__balance = 0
    self.cid = Atm.__counter
    Atm.__counter = Atm.__counter + 1
    #self.menu()

  # utility functions
  @staticmethod
  def get_counter():
    return Atm.__counter


  def get_balance(self):
    return self.__balance

  def set_balance(self,new_value):
    if type(new_value) == int:
      self.__balance = new_value
    else:
      print('beta bahot maarenge')

  def __menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()

  def create_pin(self):
    user_pin = input('enter your pin')
    self.pin = user_pin

    user_balance = int(input('enter balance'))
    self.__balance = user_balance

    print('pin created successfully')

  def change_pin(self):
    old_pin = input('enter old pin')

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input('enter new pin')
      self.pin = new_pin
      print('pin change successful')
    else:
      print('nai karne de sakta re baba')

  def check_balance(self):
    user_pin = input('enter your pin')
    if user_pin == self.pin:
      print('your balance is ',self.__balance)
    else:
      print('chal nikal yahan se')

  def withdraw(self):
    user_pin = input('enter the pin')
    if user_pin == self.pin:
      # allow to withdraw
      amount = int(input('enter the amount'))
      if amount <= self.__balance:
        self.__balance = self.__balance - amount
        print('withdrawl successful.balance is',self.__balance)
      else:
        print('abe garib')
    else:
      print('sale chor')


##############################################################Static methods
"""Points to remember about static
Static attributes are created at class level.
Static attributes are accessed using ClassName.
Static attributes are object independent. We can access them without creating instance (object) of the class in which they are defined.
The value stored in static attribute is shared between all instances(objects) of the class in which the static attribute is defined."""


class Lion:
  __water_source="well in the circus"

  def __init__(self,name, gender):
      self.__name=name
      self.__gender=gender

  def drinks_water(self):
      print(self.__name,
      "drinks water from the",Lion.__water_source)

  @staticmethod
  def get_water_source():
      return Lion.__water_source

simba=Lion("Simba","Male")
simba.drinks_water()
print( "Water source of lions:",Lion.get_water_source())