def fib(n, count=0, first=0, second=1):
    if count == n:
        return []
    return [first] + fib(n, count + 1, second, first + second)
print(fib(9))
