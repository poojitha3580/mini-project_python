word=input("enter a word:")
reverse=""
i=len(word)-1
while i>=0:
    reverse=reverse+word[i]
    i=i-1
    print("reversed word:",reverse)
    if word==reverse:
        print("palindrome")
    else:
        print("not palindrome")