num=int(raw_input())
pfactor=2;
pfact=[]
count=0
while(num>1):
	while(num%pfactor==0):
		num=num//pfactor
		count=1+count
	pfactor=pfactor+1
print(count)
