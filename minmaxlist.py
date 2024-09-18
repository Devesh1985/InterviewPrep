ls = [12,22,33,44,3,2,10,3,3]
print(min(ls), max(ls))
max=0

for i in ls:
    if i > max:
        max = i
print(max)

# ls[0], ls[-1] = ls[-1], ls[0]
# print(ls[0],ls[-1])

count=0
for i in range(len(ls)-1):
    if ls[i] ==3:
        count+=1
        if count==2:
            ls.pop(i)


print(ls)
