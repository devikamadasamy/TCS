n=int(raw_input())
l=[1]
for i in range(2,n):
	if n%i==0:
		l.append(i)
sum=0
for i in range(len(l)):
	sum=sum+l[i]
if sum==n:
	print("YES")
else:
	print("NO")
