def find_outlier(integers):
	l=len(integers)
	temp=""
	count=0
	if l<3:
		return False
	else :
		for i in range(l):
			if (integers[i]%2==0):
				count=count+1
		
		if (count>=2):
			for i in range(l):
				if (integers[i]%2==0):
					continue
				else:
					print(integers[i])

		else:
			for i in range(l):
				if (integers[i]%2==0):
					print(integers[i])
				else:
					continue

				

find_outlier([2, 4, 6, 8, 10, 3])
find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
find_outlier([160, 3, 1719, 19, 11, 13, -21])



