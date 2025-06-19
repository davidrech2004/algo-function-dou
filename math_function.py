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

def is_prime(a, i = 2, count = 1):
    if a <= 1:
        return False
    if a == 2:
        return True
    if a == i + 1:
        return count == 2
    if a % i == 0:
        return is_prime(a, i + 1, count + 1)
    return is_prime(a, i + 1, count)

def welcome():
    print("welcome to the algorithm library")

if __name__ == "__main__":
    welcome()
    print(factorial(4))
    print(is_prime(7))
    
