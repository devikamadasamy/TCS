n=raw_input()
l=map(int,n.split())
sum=0
l[0]=l[0]+1
if l[0]%2==0:
	l[0]=l[0]+1
for i in range(l[0],l[1],2):
	sum=sum+i
print(sum)
