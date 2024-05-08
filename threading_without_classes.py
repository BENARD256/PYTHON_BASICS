import threading
from threading import Thread

from time import sleep

#This program demonstrates on how to us threading with functions
def hello():
    for i in range(10):
        print("Hello")
        sleep(0.2)
def hi():
    for i in range(10):
        print("Hi")
        sleep(0.2)



process1 = Thread(target=hello)
sleep(0.9)
process2 = Thread(target=hi)


process1.start()
process2.start()

process1.join()

process2.join()
print("Executed by main Thread")
