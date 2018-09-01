binary=int(input())
i=0
decimal=0
while(binary!=0):
	p=binary%10
	decimal=decimal+p*pow(2,i)
	binary=binary//10
	i=i+1
print("decimal value "+str(decimal))

octal=int(input())
i=0
decimal=0
while(octal!=0):
	p=octal%10
	decimal=decimal+p*pow(8,i)
	octal=octal//10
	i=i+1
print("decimal value "+str(decimal))

hexadecimal=raw_input()
decimal=0
i=0
dic={"A":10,"B":11,"C":12,"D":13,"E":14,"E":15,"F":15}
for i in range(1,len(hexadecimal)+1):
	p=hexadecimal[-i]
	if p.isalpha():
		p=dic[p]
		
	else:
		p=int(p)
	decimal=decimal+p*pow(16,i-1)
print("decimalvalue "+str(decimal))
