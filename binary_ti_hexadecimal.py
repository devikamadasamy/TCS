binary=int(input())
print("binary value "+str(binary))
decimal=0
i=0
while(binary!=0):
	p=binary%10
	decimal=decimal+p*pow(2,i)
	i=i+1
	binary=binary//10
print("decimal value "+str(decimal))
hexadecimal=""
dic={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
while(decimal!=0):
	p=decimal%16
	if p>9:
		p=dic[p]
	hexadecimal=str(p)+hexadecimal
	decimal=decimal//16
print("hexadecimal value "+hexadecimal)
