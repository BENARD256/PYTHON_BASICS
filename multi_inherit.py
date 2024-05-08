"""
when working with multi level inheritance we also define the classes as demonstratred in the cons
constructor of the class that is derived from the multi level inheritance
just as shown in the sample code below

"""
class A():
    def __init__(self):
        self.a = "a"

    def printer(self):
        print(self.a)

class B():
    def __init__(self):
        self.b = "b"

    def printer(self):
        print(self.b)

class C():
    def __init__(self):
        self.c = "c"

    def printer(self):
        print(self.c)

class D(A,B,C):
    def __init__(self):
        self.d = "d"
        A.__init__(self)
        B.__init__(self)
        C.__init__(self)



    def Printer(self):
        A.printer(self)
        B.printer(self)
        C.printer(self)
        print(self.d)


obj = D()
obj.Printer()