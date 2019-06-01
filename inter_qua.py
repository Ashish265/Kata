n = int(input())
X=list(map(int,input().split()))
F=list(map(int,input().split()))
X.sort()
k_it = 0
S=[]
for ele in X:
	for j in range(F[k_it]):
		S.append(ele)
	k_it += 1


N=sum(F)
print("len",N)

val=S[:N//2]
val1=S[(N//2)+1:]
val2=S[:(N//2)]
val3=S[(N//2):]

print(val)
print(val1)
print(val2)
print(val3)


if N%2==1:
	q2=S[N//2]
	val=S[:N//2]
	q3=sum(val1[1:-1])/len(val1[1:-1])
	q1=sum(val[1:-1])/len(val[1:-1])
	print(round(q3-q1,1))
else:
	q2=(S[(N//2)-1]+S[(N//2)])/2
	if len(val2)%2==1:
		q1=val2[len(val2)//2]
		q3=val3[len(val3)//2]
		print(q3)
		print(q1)

		print(round(q3-q1,1))
	else:
		q3=(val3[(len(val3)//2)-1]+val3[len(val3)//2])/2
		q1=(val2[(len(val2)//2)-1]+val2[len(val2)//2])/2
		print(round(q3-q1,1))
		print(q3)
		print(q1)