def findsum(ls, total):
    l = 0
    r = len(ls)-1
    res = []
    ls.sort()

    while r>l:
        if ls[r] + ls[l] == total:
            res.append([ls[r],ls[l]])
            r-=1
            l+=1
        elif ls[r] + ls[l] > total:
            r -= 1
        elif ls[r] + ls[l] < total:
            l +=1
    print(res)

ls = [5,7,4,3,9,8,19,11]
total = 17
findsum(ls, total)