d1 = {'a':'raja', 'b':'baoy'}
d2 = {'g':'google', 'r':'niop'}
d1.update(d2)
print(d1)

res = {**d1, **d2}
print(res)

d1.update(d2)

def withDict():
    st = "aabbbcddeeee"
    res = {}
    for i in st:
        res[i] = st.count(i)
    fn = sorted(res.items(), key=lambda x:x[1])
    print(fn[-2][0])

def withCount():
    st = "aabbbcddeeee"
    res =[]
    for i in st:
        if [i,st.count(i)] not in res:
            res.append([i,st.count(i)])
    res.sort(key = lambda x:x[1])
    print(res[-1][0])


withDict()
withCount()
