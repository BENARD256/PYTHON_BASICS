#Functions in python
"""

FUNCTIONS CONTAIN A BLOCK OF CDE

"""


#kwargs functions : In this arguments a defined before they are utilized by the user


def bio(name="Anzo", age=10, dept="ict"):

    print(
        name,
        age,
        dept
    )

bio("Anzo Benarf", dept="COdE")


#*params arguments : This is of type tuple and using a for loop it can be itetated to add the the values to the sam variable

def add(*params):
    sum = 0
    for num in params:
        sum += num

    print("Total: %d"%(sum))

add(10, 10, 10, 10,10)



#**dict
def ad(**dict):
   for key, val in dict.items():
       print(key, val)
ad(a=1, b=2)


#recursion of a function

"""
REcursion is the act of making a function call it self this is a key thing in the world of software developments

"""

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num -1)
val = factorial(12)
print(val)

"""Working with lamda functions in python These function dont have a body"""


half = lambda x:x//2
double = lambda x:x*2
s_root = lambda x :x**2
cube = lambda x:x**3


answer = cube(10)
print(answer)

"""
using the map function
Takes a function and the values to apply to it
"""


value  = map(lambda x:x*2, range(1, 11))

print(value)