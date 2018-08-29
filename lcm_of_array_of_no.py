def find_lcm(num1,num2):
	minimum=min(num1,num2)
	for i in range(1,minimum//2+1):
		if num1%i==0 and num2%i==0:
			gcd=i
	
	lcm=(num1*num2)//gcd
	return lcm

n=raw_input()
l=map(int,n.split())
 
num1 = l[0]
num2 = l[1]
lcm = find_lcm(num1, num2)
 
for i in range(2, len(l)):
    lcm = find_lcm(lcm, l[i])
     
print(lcm)
