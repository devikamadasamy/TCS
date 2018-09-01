n=raw_input()
count=0
count1=0
for i in range(len(n)):
	if(n[i]=="("):
		count=count+1
	if(n[i]==")"):
		count1=count1+1
if count==count1:
	print(count)
else:
	print("-1")
