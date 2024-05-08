class car():
    def __init__(self):
        self.color = "Black"
        self.wheels = 4
        self.oil = "Petrol"
        self.door= 4


    def set_color(self, color):
        self.color = color
    def get_color(self):
        print("Color: %s"%(self.color))

    def set_wheels(self, wheels=4):
        self.wheels = wheels
    def get_wheels(self):
        print("Wheels: %s"%(self.wheels))

    def set_oil(self, oil="Petrol"):
        self.oil = oil
    def get_oil(self):
        print("Oil Used: %s" % (self.oil))

    def set_door(self ,doors=4):
        self.door = doors
    def get_door(self):
        print("Doors: %s" % (self.door))


class lamboghin(car):
    def __init__(self):
        print("Lambo...")

    #Method only defined in lambo class
    def autopilot(self, on=True):
        if on == True:
            print("Auto pilot is enabled")
        else:
            print("Autopilot is Disabled")


lb = lamboghin()
lb.set_color("Red")
lb.get_color()

lb.set_door(2)
lb.get_door()

lb.set_wheels(5)
lb.get_wheels()

lb.set_oil("Diesel")
lb.get_oil()
lb.autopilot(on=False)

