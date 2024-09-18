def findword(sent):
    ls = sent.split(" ")
    mx = 0
    word = []
    for i in range(len(ls)):
        if len(ls[i])%2 == 0:
            if len(ls[i]) > mx:
                mx = len(ls[i])
                word.append([ls[i], mx])
    print(word, mx)
    if mx != 0:
        return word[-1][0]
    else:
        return "00"

print(findword("this is me, and i will do everything to clear interview"))