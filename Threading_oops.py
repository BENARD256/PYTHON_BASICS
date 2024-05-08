'''
threading in python allows execution of code on multiple cores of the cpu

initially the program is executed on the by the main thread
however threads can be created so that classes of a program are executed simultaniously

To do :
Each class must override the Run method of the threads class

the methods in the class can later be called using the start() method that tell the thread to exec

'''
from threading import Thread
from time import sleep


class hello(Thread):

    def run(self):
        for i in range(10):
            print("Hello")
            sleep(0.5)

class hi(Thread):

    def run(self):
        for i in range(10):
            print("Hi")
            sleep(0.5)

t1 = hello()
t2 = hi()

t1.start()
sleep(1) #This initiated a time btn the threads so that the threads do collide when being executed
t2.start()


#The Join can help when we want the main thread to execute after all the 2 Threads are completed
t1.join()
t2.join()
main_thread = "Printed by Main Thread"
print(main_thread)