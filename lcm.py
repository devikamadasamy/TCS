def gcd(m,n):
	cf=[]
	k=m*n
	
	for i in range(1,min(m,n)+1):
		if m%i==0 and n%i==0:
			cf.append(i)
	lcm=k//cf[-1]
	print(lcm)
a=int(input())
b=int(input())
gcd(a,b)
