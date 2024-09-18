def fibonaci(num):
    a = 0
    b = 1
    print(a, b, end="/n")
    while True:
        c = a+b
        yield c
        a, b = b,c

res = fibonaci()
for i in res(10):
    print(i)



