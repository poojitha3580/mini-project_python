text=input("enter a string:")
max_char=""
max_count=0
for ch in text:
    count=text.count(ch)

    if count>max_count:
        max_count=count
        max_char=ch
        print("most frequent character:",max_char)
