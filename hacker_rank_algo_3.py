num = list(map(int,input().split()))
for k in range(len(num)):
    j=max(range(num[k]))+1
    i=1
    while i <=j:
        if i % 3 !=0 and i%5 !=0:
            print(i)
        elif i%3==0 and i%5!=0:
            print("Fizz")
        elif i %3!=0 and i%5==0:
            print("Buzz")
        elif i%3==0 and i%5==0:
            print("FizzBuzz")
        i+= 1