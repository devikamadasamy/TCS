n=raw_input()
list1=["a","e","i","o","u","A","E","I","O","U"]
string=""
for i in range(len(n)):
	if n[i] not in list1:
		string=string+n[i]
print(string)
