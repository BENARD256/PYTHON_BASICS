'''
EXCEPTIONS CAN BE DEFINED BY CREATING A CLASS THAT INHERITS FROM THE EXCEPTION CLASS
AND ALSO USING THE STRINGFY METHOD TO DISPLAY THE ERROR MESSAGE TO DISPLAY IF AN ERROR OCCURED

'''
class ModulusError(Exception):
    def __init__(self, a):
        self.a =0


    def __str__(self):
        error = str("Error Expected Result of Modulus Computation to be 0")

        return error




def mod(a):
    c= a%2
    if c == 0:
        print("Result: %d"%(c))
        print("%d is a Prime Number"%(a))

    else:
        raise ModulusError(a)
    return True


try:
    mod(-3)
except ModulusError as er:
    print(er)
