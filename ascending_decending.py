# your code goes here
n=raw_input()
l=map(int,n.split())
no=len(l)
	
p=no//2
if no%2!=0:
	p=p+1
first=l[:p]
for i in range(len(first)-1):
	min=first[i]
	pos=i
	for j in range(i+1,len(first)):
		if first[j]<min:
			min=first[j]
			pos=j
	(first[pos],first[i])=(first[i],first[pos])
	
print(first)
		
second=l[p:]
for i in range(len(second)-1):
	max=second[i]
	pos=i
	for j in range(i+1,len(second)):
		if second[j]>max:
			max=second[j]
			pos=j
	(second[pos],second[i])=(second[i],second[pos])
print(second)
last=first+second	
print(last)
string=""
for i in range(len(last)-1):
	string=string+str(last[i])+" "
string=string+str(last[len(last)-1])
print(string)
	
