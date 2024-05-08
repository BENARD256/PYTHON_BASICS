'''
Inheritance ability of a child class to  obtain features of its parent class
Behavour of constructor with inheritance
Multi-level inheritance When  a class is inheriting from a class that is a child class to a nother parent class
Multiple inheritance(When a class inherits from more than one class
MRO: Method Resolution Order : This is the order in which Inits or methods are exec from the inheritedclass

MRO counts from the left to the right hand
'''

class A:
    def __init__(self):
        print("A init")
    def method(self):
        print("Method A")

class B:
    def __init__(self):
        print("B init")
    def method(self):
        print("Method B")

class C:
    def __init__(self):
        print("C init")
    def method(self):
        print("Method C")

class D(A,B,C):#multiple inheritance
    def __init__(self):
        super().__init__()
        print("D init")

    def method(self):
        super(A, self).method()
        super(D, self).method()

        print("Method D")
#if the child class doesnt have a init it will refer to that of the child class
obj = D()

obj.method()