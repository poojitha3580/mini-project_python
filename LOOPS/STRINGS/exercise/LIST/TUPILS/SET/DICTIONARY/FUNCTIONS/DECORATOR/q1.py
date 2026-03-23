def decorator (func):
    def wrapper():
        print("before execution")
        func()
        print("after execution")
    return wrapper
def greet():
    print("hello!")
greet= decorator(greet)
greet()