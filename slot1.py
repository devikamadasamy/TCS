n=int(raw_input())
if n%2!=0:
	list1=[1]
	p=n//2+1
	prod=1
	for i in range(1,p):
		prod=prod*2
		list1.append(prod)
	print(list1[-1])
else:
	p=n//2
	prod=1
	list2=[1]
	for i in range(1,p):
		prod=prod*3
		list2.append(prod)
	print(list2[-1])
