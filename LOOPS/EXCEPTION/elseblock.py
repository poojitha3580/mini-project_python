try:
    num=int(input("enter a number:"))
    print(10/num)
except ZeroDivisionError:
    print("cannot bdivide by zero")
except ValueError:
    print("Invalid Input")
else:
    print("No Error Occured")