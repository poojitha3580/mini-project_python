stack=[7,25,32]
if len(stack)==0:
    print("stack underflow")
else:
    removed = stack.pop()
    print("popped element:",removed)
print("stack after pop:",stack)