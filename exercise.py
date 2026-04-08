class stack:
    def __init__(Self,size):
        Self.stack=[]
        Self.size=size
    def push(Self,value):
        if len(Self.stack)==Self.size:
            print("stack overflow")
        else:
            Self.stack.append(value)
            print(value,"pushed")
    def pop(Self):
        if len(Self.stack)==0:
            print("stack underflow")
        else:
            print(Self.stack.pop(),"popped")
    def peek(Self):
        if len(Self.stack)==0:
            print("stack is empty")
        else:
            print("top:",Self.stack[-1])
    def isempty(Self):
        return len(Self.stack)==0
    def isfull(Self):
        return len(Self.stack)== Self.size
    def display(Self):
        print("stack:",Self.stack)
s=stack(3)
s.push(10)
s.push(20)
s.push(30)
s.push(40)

s.display()

s.pop()
s.peek()
print("empty?",s.isempty())
print("full?",s.isfull())

