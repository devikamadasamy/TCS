n=int(input())
print("decimal value"+str(n))
decimal=n
nn=n
nnn=n

bina=""
while(nnn!=0):
	p=nnn%2
	bina=str(p)+bina
	nnn=nnn//2
print("binary value "+bina)

sum=""
while(nn!=0):
	p=nn%8
	sum=str(p)+sum
	nn=nn//8
print("octal value "+sum)

sum=""
dic={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
while(n!=0):
	p=n%16
	if(p>9):
		p=dic[p]
	sum=str(p)+sum
	n=n//16
print("hexadecimal value "+sum)

sevenbase=""
while(decimal!=0):
	p=decimal%7
	sevenbase=sevenbase+str(p)
	decimal=decimal//7
print("seven base "+sevenbase)
