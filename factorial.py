def factorial(num):
    sp = num-1
    bp = num* num-1
    if num ==1:
        return 1
    return  num * factorial(num-1)


print(factorial(5))
