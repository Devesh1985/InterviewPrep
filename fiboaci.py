def fib(limit):
    a = 0
    b = 1
    c= a+b
    while c < limit:
        c = a+b
        print(c)
        a=b
        b=c


fib(13)