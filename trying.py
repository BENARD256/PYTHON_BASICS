"""Exeption handling in python


user can define there own exeptions

using the raise key word
"""


def function(x):
    if x < 0:
        raise ValueError("The value is less than 0 ")
    else:
        print("Greater than 0")


try:
    function(-1)

except ValueError as e:
    print(e)
else:#Exec if no error is hit during exec of code in the try block
    print("provided all goes good i will run")

finally:#exec if every thing happens

    print("regardless i still run")