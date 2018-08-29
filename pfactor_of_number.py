num=int(raw_input())
pfactor=2;
pfact=[]
while(num>1):
	flag=0
	
	while(num%pfactor==0):
		num=num//pfactor
		flag=1
	if flag==1:
		pfact.append(pfactor)
		
	pfactor=pfactor+1
string=""
for i in range(len(pfact)-1):
	string=string+str(pfact[i])+","
string+=str(pfact[len(pfact)-1])
print(string)
