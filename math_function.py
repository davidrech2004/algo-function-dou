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

def is_prime(a, i = 2):
    if (a % i == 0 and i != a) or a == 1:
        return False
    if a == i:
        return True
    return is_prime(a, i + 1)

def welcome():
    print("welcome to the algorithm library")

if __name__ == "__main__":
    welcome()
    print(factorial(4))
    print(is_prime(1))
    
