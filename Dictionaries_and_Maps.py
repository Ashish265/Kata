n = int(input())
phoneBook = {}
for i in range(n):
    name,phn = input().split()
    phoneBook[name] = phn
while True:
    try:
        query = input()
        if not query.strip():
            break
        if query in phoneBook.keys():
            print(query+"="+phoneBook[query])
        else:
            print("Not found")
    except:
        break