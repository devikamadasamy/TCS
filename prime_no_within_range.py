string=raw_input()
list1=map(int,string.split())
list2=[]
for i in range(list1[0]+1,list1[1]):
	fact=0
	for j in range(2,i//2+1):
		if(i%j==0):
			fact=1
			break
	if fact==0:
		list2.append(i)
sum=0
for i in range(len(list2)):
	sum=sum+list2[i]
print(sum)
