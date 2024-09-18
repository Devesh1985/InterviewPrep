"""Write a Python program to check whether a given string contains a capital letter,
a lower case letter, a number and a minimum length.
W3resource"""
def checkPass(str, min):
    expected = ['min', 'cap', 'lower', 'number']
    auth= []
    if len(str) >= min:
        auth.append('min')
        for i in str:

            if i.islower() == True:
                print(f"lower {i}")
                if 'lower' not in auth:
                    print(f"lower {i}")
                    auth.append('lower')
            elif i.isupper():
                print(f"upper {i}")
                if 'cap' not in auth:
                    print(f"upper {i}")
                    auth.append('cap')
            elif i.isnumeric():
                print(f"numeric {i}")
                if 'num' not in auth:
                    print(f"numeric {i}")
                    auth.append('num')
    print(auth)
    if auth.sort() == expected.sort():
        print(f"validation is good")


checkPass("W3resource", 8)