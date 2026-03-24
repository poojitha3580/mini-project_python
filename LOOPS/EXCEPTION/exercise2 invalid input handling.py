try:
    num=int(input("enter a number"))
    print(num)
except InvalidInputError:
    print("error:InvalidInputError")