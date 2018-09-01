n=raw_input()
l=map(int,n.split())
k=int(raw_input())
out=[]
for i in range(len(l)):
	if l[i]<k:
		out.append(l[i])
string=""
for i in range(len(out)-1):
	string=string+str(out[i])+" "
string=string+str(out[len(out)-1])
print(string)
