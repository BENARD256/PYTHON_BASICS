"""
by default iterator are employed using the for loop

In oops iterated can be by overriding the iter and next methods
The result can be printed by making a for loop to iterator the elementes of the class object created

"""
class iterator:
    def __init__(self, iterations=0):
        print("iterator init ")
        self.counter = 0
        self.iterations = iterations #This is the counter for the iteration

    def __iter__(self):
        return self


    def __next__(self):

        if self.counter <= self.iterations:
            var = self.counter
            self.counter +=1

        else:
            raise StopIteration

        return var


obj = iterator(iterations=10)

while True:
    print(next(obj))