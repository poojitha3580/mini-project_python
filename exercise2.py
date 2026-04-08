class stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, value):
        if self.isfull():
            print("stack overflow!")
        else:
            self.stack.append(value)
            print(value, "pushed")

    def pop(self):
        if self.isempty():
            print("stack underflow!")
        else:
            print(self.stack.pop(), "popped")

    def peek(self):
        if self.isempty():
            print("stack is empty")
        else:
            print("top:", self.stack[-1])

    def isempty(self):
        return len(self.stack) == 0

    def isfull(self):
        return len(self.stack) == self.size

    def display(self):
        print(self.stack)


s = stack(5)

while True:
    print("\n--stack menu---")
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.isempty")
    print("5.isfull")
    print("6.display")
    print("7.exit")

    choice = int(input("enter choice: "))

    if choice == 1:
        val = int(input("enter value: "))
        s.push(val)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        print(s.isempty())

    elif choice == 5:
        print(s.isfull())

    elif choice == 6:
        s.display()

    elif choice == 7:
        break