def find_short(s):
    # your code here
    a=s.split()
    print(a)	
    lent=[]
    for elem in a:
    	lent.append(len(elem))
    l=min(lent)
    print(l)

    return l # l: shortest word length





find_short("bitcoin take over the world maybe who knows perhaps")
find_short("turns out random test cases are easier than writing out basic ones")
find_short("lets talk about javascript the best language")
find_short("i want to travel the world writing code one day")
find_short("Lets all go on holiday somewhere very cold")