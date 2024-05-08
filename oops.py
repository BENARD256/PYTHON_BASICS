class human:
    def __init__(self):
        print("The human Class")
    def show(self):
        print("General Information for all Humans")

    def set_name(self, name):
        self.name = name
        print("Name updated")

    def get_name(self):
        print("Name: "+self.name)
#using the class to pring general information for all users



#Child class Male
class male(human):
    def __init__(self):
        print("Gender: Male")
    #polymorphism in the male class We are to modifiy the functionality of get name to only male
    def get_name(self):
        print("This is modified in Male class")

        print("Name: "+self.name)

#Chil class Female
class Female(human):
    def __init__(self):
        print("Gender: Female")

human().show()
print()
Benard = male()
Benard.set_name("Anzo Benard")
Benard.get_name()

print()
#object for female class

shakira = Female()
shakira.set_name("Shakira S")
shakira.get_name()



print("Ehlldfifjfpd", sep=)