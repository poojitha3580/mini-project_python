a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
min1= a if a<b else b
minimum= min1 if min1<c else c
print("minimum numberis:",minimum)