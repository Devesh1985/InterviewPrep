"""Given a string input, if the input string length is odd, then return the string with the middle three letters. If the length is less than or equal to 3, then return as it is.
Input: “NewMumbai” or “New”
Output: Mum or New"""
def strFromtat():
    st = "New"

    if len(st) < 3:
        return st
    elif len(st)%2!=0:
            mid = len(st)//2
            return st[(mid-1):((mid-1)+3)]


print(strFromtat())