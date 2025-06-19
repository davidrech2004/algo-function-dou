def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a - 1)

def welcome():
    print("welcome to the algorithm library")

if __name__ == "__main__":
    welcome()
    print(factorial(4))
    
