def remveDuplicate(ls):
    temp = []
    for i in range(len(ls)-1):
        if ls[i] == ls[i+1]:
            continue
        else:
            temp.append(ls[i])
        # temp.append(ls[i])
    temp.append(ls[-1])
    print(temp)





ls = [5,5,9,9,9,7,8,8,11,11,11]
remveDuplicate(ls)