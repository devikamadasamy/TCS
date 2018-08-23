p=int(raw_input())
string=raw_input()
list1=["a","e","o","u","A","E","I","O","U"]
output=""
for i in range(len(string)):
	if string[i] not in list1:
		output=output+string[i]
out=""
for i in range(1,len(output)+1):
	out=out+output[-i]
print(out)
