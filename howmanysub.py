n=raw_input()
sub=raw_input()
count=0
for i in range(len(n)-2):
	substring=n[i]+n[i+1]+n[i+2]
	if substring==sub:
		count=count+1
 
print(count)
