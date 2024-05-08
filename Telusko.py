import os
from os import system
from os import getcwd
from os import path
#cd = os.getcwd()

for dir, file, pt in os.walk(os.getcwd()):
    """
    if "libraries" in dir:
        print(dir)
        os.chdir(dir)
        print(os.getcwd())
        system("touch deques.py")
    """
    #print(pt)