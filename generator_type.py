
#The generator command can be used to accomplish various concepts in the background such as Checking spelling in the back ground
from time import sleep
def generator():
    for i in range(1, 11):
        print("Calling %d"%(i))
        yield i
        sleep(1)
var = generator()


try:
    for i in range(1, 110):
        var.__next__()
except StopIteration:
    print("Iteration out of range")

except Exception:
    print("Exeption occured")
finally:
    print("Execution is complete")