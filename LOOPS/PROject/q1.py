def natural_numbers(n):
    print("natural numbers series:")
    for i in range(1, n+1):
        print(i,end=" ")
    print()
def even_numbers(n):
    print("even numbers series:")
    for i in range(2, n+1,2):
        print(i, end=" ")
    print()
def odd_numbers(n):
    print("odd number series:")
    for i in range(1,n+1,2):
        print(i,end=" ")
        print()
def fibonacci(n):
    print("fibonacci series:")
    a,b=0,1
    for i in range(n):
        print(i,end=" ")
        a,b=b, a+b
    print()
print("number series generator")
print("1.natural numbers")
print("2.even numbers")
print("3.odd numbers")
print("4.fibonacci series")

choice=int(input("enter your choice:"))
n=int(input("enter the limit:"))
if choice==1:
    natural_numbers(n)
elif choice==2:
    even_numbers(n)
elif choice==3:
    odd_numbers(n)
elif choice==4:
    fibonacci(n)
else:
    print("invalid choice")