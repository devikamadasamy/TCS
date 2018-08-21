import sys
if len(sys.argv) == 2:
    n=int(sys.argv[1])
#for i in range(number):
 #   print("hello")
if n%2==0:
	n=n//2
	count=1
	list1=[2]
	if n==1:
		print("2")
	else:
		i=3
		while(count<n):
			flag=0
			for j in range(2,i):
				if i%j==0:
					flag=1
					break
			if flag==0:
				list1.append(i)
				count=count+1
			i=i+1
	
		print(list1[-1])
else:
	n=n//2+1
	list2=[1,1]
	if n==1 or n==2:
		print("1")
	else:
		for i in range(2,n):
			list2.append(list2[i-1]+list2[i-2])
		print(list2[-1])
