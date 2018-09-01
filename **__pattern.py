n=int(raw_input())
pi=[]
for i in range(1,n+1):
	string=""
	for j in range(i-1):
		string=string+str(i)+"*"
	string=string+str(i)
	pi.append(string)
	print(string)
d=len(pi)
for i in range(len(pi)-1):
	print(pi[-i-2])
