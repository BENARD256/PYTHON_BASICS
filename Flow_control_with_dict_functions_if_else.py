#Creating a dictionary of functins so that they can be implemented in a control statement

"""USING DICTIONARY TO CONTROL FLOW AS WELL AS FUNCTIONS """
def copy():
    print("Copying....")


def paste():
    print("Pasting....")


def exiting():
    print("Exiting....")


dict = {}

dict["copy"] = copy
dict["paste"] = paste
dict["exit"] = exiting

cmd = input("Enter Command: ")



if dict.get(cmd) != None:

    dict[cmd]()
else:
    print("\nPlease Enter a valid key")
