"""count char """
def charmaxCount(ar):

    res =[]
    mx = 0
    count = 1
    for i in range(len(ar)-1):
        if ar[i] == ar[i+1]:
            count += 1
            continue
        else:
            if mx < count:
                mx = count
                count = 1
                res.append([ar[i], mx])
    if mx < count:
        res.append([ar[-1], count])
    print(res)


def charCount(ar):
    res = ""
    ls = []
    count = 0
    for i in ar:
        if i not in res:
            # ls.append(i)
            res = res + str(ar.count(i)) + i
    print(res)





ar = "aaaabbcdefff"
charmaxCount(ar)
charCount(ar)
