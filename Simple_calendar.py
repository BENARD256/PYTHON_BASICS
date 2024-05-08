import calendar
from calendar import calendar
def cal():

    yr = int(input("Enter Calender Year: "))
    c = calendar(yr)

    print(c)


if __name__ == "__main__":
    cal()