n=input()
p=""
for i in range(1,len(n)+1):
	p=p+n[-i]
print(p)
if p==n:
	print("palindrome")
else:
	print("not a palindrome")
