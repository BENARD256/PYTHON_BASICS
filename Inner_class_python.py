"""
Inner class is a class that is defined insided a class
Below is the implementation of a inner class insided the Student's class


"""
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.pc_type = self.inner()

    def info(self):
        print("Name: %s"%(self.name))
        print("Roll: %s" % (self.roll))


    class inner:
        def __init__(self):
            self.pc = "\"Lenovo T470s\""

        def get_pc(self):
            print("PC IS "+str(self.pc))




st = Student(roll=1001, name="Anzo Benard").inner()#creating object for the inner class


st.get_pc()## Accessing the method of the inner class