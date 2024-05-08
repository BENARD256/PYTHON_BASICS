"""
DUCK TYPING is a way of implementing polymorphism
if anything walks, quarkm and swims like a duck then its a aduck

so regardless of the class provided it has the method that is in common in another class the same funct
can be called

"""
class Notepad:
    def __init__(self):
        print("init in Notepad")

    #operator Overloading
    def exec(self):
        print("Execiting ..........")
        print("Compiling ..........")
        print("Completed ..")

class Vs:
    def __int__(self):
        print("Init in vs")

    def exec(self):
        print("Vs checking on the spelling")
        print("vs Eliminating errors")
        print("Execiting ..........")
        print("Compiling ..........")
        print("Completed ..")


class python:
    def __int__(self):
        print("Python Programming language")

    def ide(self, run):#run is a variable that is used to create an object of the editor class so th
        run.exec()

#since the method is defined in both the editor classes regardless of the editor obj it can be accessed

a = python()
#In order to call the ide method we pass it an arg of an object of the editor
editor = Vs()

a.ide(editor)


