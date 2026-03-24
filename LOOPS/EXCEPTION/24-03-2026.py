try:
    num1=int(input("enter first number"))
    num2=int(input("enter second number"))
    print("choose operation:+,-,*,/")
    op=input("enter operator:")

    if op=="+":
        print("result:", num1+num2)
    elif op=="-":
        print("result:",num1-num2)
    elif op=="*":
        print("result:",num1*num2)
    elif op=="/":
        print("result:",num1/num2)
    else:
        print("invalid operator")
except ZeroDivisionError:
    print("error: cannot divide by zero")
except ValueError:
    print("error:",ValueError)
except TypeError:
    print("error:",TypeError)
except KeyError:
    print("error:",KeyError)