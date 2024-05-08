
from abc import ABC, abstractmethod

"""
Abstact is the ability to work without the need to understand the underlaying structure of the
methods being useds in the codebasae your using
provided the functionality that you want is achieved

ABSTRACT isnt supported in python by default so we use the ABC(Abstact Base Class Module)

while working with abstract obj of abstract classes cant be created but a child class of it
can inherit the methods of the abstract class
"""

class A(ABC):
    def __init__(self):
        print("A init")

    @abstractmethod
    def info(self):
        pass #Just initialized


class B(A):
    def __init__(self):
        print("B Init")
        

    def info(self):
        print("Applied in class B")



s1 = B()

s1.info()