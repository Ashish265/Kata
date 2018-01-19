# return masked string
def is_isogram(string):
    #your code here
    string=string.casefold()
    print(string)
    l=len(string)
    #print(l)
    for i in range(len(string)):
    	#print("for i =",i)
    	for j in range(i):
    		#print("for j =", j)
    		if string[i]==string[j]:
    			print(string[i])
    			return False
    else:
    	print("isogram")
    	return True
    		





is_isogram("moOse")
is_isogram("Dermatoglyphics")
is_isogram("aba")
is_isogram("isogram")
is_isogram("isIsogram")

