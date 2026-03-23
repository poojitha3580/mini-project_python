a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
d=int(input("enter a number:"))
min1= a if a<b else b
min2= min1 if min1<c else c
minimum= min2 if min2<min1 else d
print("minimum numberis:",minimum)