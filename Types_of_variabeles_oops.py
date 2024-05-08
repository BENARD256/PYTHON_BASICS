'''
Types of Variables in oops
Instance Variables Variables defined in the init of the class
Class Variables These are defines outside the init but still inside the class

changing an instance variables Doesn't change the value of the variables for other objects

Changing the Class variable Value changes the value of the Variables for all objects of the class

Class varibles can be accessed using the class name


'''
class Car():
    wheels = 4
    def __init__(self):
        self.color  = "Black"

Car.wheels = 10
obj1 = Car()
obj2 = Car()
#changing the instance Variable
obj1.color = "Red"
#Changing the value of Wheels using the class affects all objects of the class

print(obj1.color, obj2.color)
print(obj1.wheels, obj2.wheels)
