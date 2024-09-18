"""write a python program to print the char and their count
 input = "aaaabbbccd"
ouput = 4a3b2c1d
"""

def charCount(st):
    res = ""
    for i in st:
        if i not in res:
            res= res+ str(st.count(i))+i
    print(res)





st = "aaaabbbccd"
charCount(st)