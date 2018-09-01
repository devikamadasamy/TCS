num1=raw_input()
num2=raw_input()
count=0
for i in range(len(num1)):
	if num1[i]==num2:
		count=count+1
print(count)
