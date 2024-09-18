import pytest

def test_swapnum():
    n1 = 19
    n2 = 88
    n1,n2 =n2,n1
    print(n1, n2)

@pytest.mark.parametrize(argnames='num', argvalues=[3,4,5,6,7,8,9,10,11,12,13])
def test_primeornot(num):
    flag = True
    for i in range(2,10):
        if num!=i:
            if num%i !=0:
                continue
            else:
                flag=False
                break
    print(flag)







