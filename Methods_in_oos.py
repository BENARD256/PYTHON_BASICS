'''
In oops there  there are 3 categories of methods that can be used in oops
Instance methods these are used to handle and deal with instance methods
Class Methods these are utliized when working with class variables which and a cls key word used
Static method these are used to handle any argument that ain't related to anything


categories of Instance Methods
these are categorised inot Mutators and Accessor


'''

class Student():
    school  = "Isbat university"
    def __init__(self):
        self.name = ""
        #instance  Methods ie Accessors and Mutators
    #Mutators
    def set_name(self, name):
        self.name = name
    #Accessor
    def get_name(self):
        print("Name: %s"%(self.name))
    #class methods
    @classmethod
    def info(cls):
        print("University: %s"%(cls.school))

    #Static Methods : These are  used to just print and take no args
    @staticmethod
    def static_method():
        print("Information From static method")

anzo = Student()
anzo.set_name("Anzo Benard")
anzo.get_name()

Student.info()
Student.static_method()#Static method can be printed using the class name
#if Obj is used to Access a static positional Args error will be thrown


