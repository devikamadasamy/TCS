n=int(raw_input())
flag=0
for i in range(2,n):
	if n%i==0:
		flag=1
		break
if flag==0:
	ans=float(n)**(0.5)
	ans=round(ans,2)
	print(ans)
else:
	print("0.00")
	
