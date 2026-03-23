text=input("enter a string:")
upper=0
lower=0
digit=0
special=0
for ch in text:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digit+=1
    else:
        special+=1
print("uppercase:",upper)
print("lowercase:",lower)
print("digits:",digit)
print("special characters:",special)