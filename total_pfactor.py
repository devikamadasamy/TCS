num=int(raw_input())
pfactor=2;
pfact=[]
total_count=0
while(num>1):
	count=0
	
	while(num%pfactor==0):
		num=num//pfactor
		count=1+count
	if count!=0:
		print(str(pfactor)+":"+str(count))
		total_count+=count
		
	pfactor=pfactor+1
print(total_count)
