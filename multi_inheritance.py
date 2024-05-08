#Multi level inheritance
class A:
    def __init__(self):
        print("Class A constructor")
    def A(self):
        print("method in A")
class B:
    def __init__(self):
        print("Class B constructor")


    def B(self):
        print("Method in B")

class C:
    def __init__(self):
        print("Class C Constructor")
    def C(self):
        print("Method in C")

class D:
    def __init__(self):
        print("Class D Constructor")


    def D(self):
        print("Method in D")

class E(A,B,C,D):
    def __init__(self):
        print("Class E Constructor")
    def E(self):
        print("Method in E")


obj = E()
obj.A()
obj.B()
obj.C()
obj.D()
obj.E()




