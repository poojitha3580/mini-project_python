text=input("enter a string:")
results=""
for ch in text:
    if ch not in results:
        results+=ch
print("string without duplicates:",results)