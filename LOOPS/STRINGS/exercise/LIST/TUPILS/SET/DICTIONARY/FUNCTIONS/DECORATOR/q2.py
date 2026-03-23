def decorator (func):
    def wrapper(name):
        print("before execution")
        func(name)
        print("after execution")
    return wrapper
def greet (name):
    print(f"olive{name}")
greet("adam")