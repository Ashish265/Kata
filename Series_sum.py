def series_sum(n):
    # Happy Coding ^_^
    sum=0
    for i in range(n):
    	sum=sum+(1/(1+(3*i)))
    	#sum=round(sum,3)
    sum=round(sum,2)
    print(sum)
    return (sum)
series_sum(39)