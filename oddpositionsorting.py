arr=raw_input()
l=map(int,arr.split())
lee=[]
for i in range(0,len(l),2):
	lee.append(l[i])
for i in range(len(lee)-1):
	min=lee[i]
	pos=i
	for j in range(i,len(lee)):
		if lee[j]<min:
			min=lee[j]
			pos=j
	(lee[pos],lee[i])=(lee[i],lee[pos])
print(lee)
string=""
print(l)
pi=[]
j=1
for i in range(len(lee)-1):
	pi.append(lee[i])
	pi.append(l[j])
	j=j+2
if(len(l)%2==0):
	pi.append(lee[len(lee)-1])
	pi.append(l[len(l)-1])
else:
	pi.append(lee[len(lee)-1])
print(pi)
	
string=""	
for i in range(len(pi)-1):
	string=string+str(pi[i])+","

string=string+str(pi[len(pi)-1])
print(string)
	
	
