n=int(input())
if n%2!=0:
	list1=[0]
	p=n//2+1
	sum=0
	for i in range(1,p):
		sum=sum+2
		list1.append(sum)
	print(list1[-1])
else:
	list2=[]
	p=n//2
	sum=0
	for i in range(1,p):
		sum=sum+1
		list2.append(sum)
		
	print(list2[-1])	
