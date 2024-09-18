def sumArray():
    ls = [4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
    current = 0
    max = 0
    for i in ls:
        current = current+ i
        if current > max :
            max = current
        elif current < 0:
            current =0
    print(max)

sumArray()