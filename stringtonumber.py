"""Write a Python program that takes a string and replaces all the characters with their respective numbers.
Sample Data:
("Python") -> "16 25 20 8 15 14"
("Java") -> "10 1 22 1"
("Python Tutorial") -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"""


def strtonum(s1):
    ls = "abcdefghijklmnopqrstuvwxyz"
    ls = ",".join(ls)
    res = ls.split(",")
    fn = []
    for i in range(len(s1)):
        fn.append(res.index(s1[i].lower())+1)
    print(fn)

s1 ="Python"
strtonum(s1)
