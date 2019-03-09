def gcdIter(a, b):
    test_Value = min(a,b)
    while a%test_Value !=0 or b%test_Value !=0:
        test_Value = test_Value - 1
    print(test_Value)
    return  test_Value 

gcdIter(2,12)
gcdIter(5,12)
gcdIter(17,8)
gcdIter(234, 54)
gcdIter(144, 56)