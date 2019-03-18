import re
import sys
import os

N = int(input("Enter the Number of inputs : "))

phone_n = []
for i in range(N):
    a = input("Enter the number : ")
    phone_n.append(a)
    
for ele in phone_n:
	if re.match(r'[7-9]{1}[0-9]{9}',ele) and len(ele)==10:
		print("YES")
	else:
		print("NO")