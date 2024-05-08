class A():
    def __init__(self):
        print("In A init")

    def A(self):
        print("In A")
class B(A):
    def __init__(self):
        print("In B init")
        super().__init__()

    def B(self):
        print("In b")
class C(B, A):
    def __init__(self):
        print("In C init")
        super().__init__()
    def C(self):
        print("In C")
        super().A()
        super(C, self).B()

""""
In order You want to Access the inits of the the other classes we user the super key work
"""



obj1 = C()

obj1.C()