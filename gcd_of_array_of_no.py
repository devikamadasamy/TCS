import sys
no_list=[]
if(len(sys.argv)!=1):
    for i in range(1,len(sys.argv)):
        no_list.append(int(sys.argv[i]))
#n=raw_input()
#no_list=map(int,n.split())
minimum=min(no_list)
for i in range(1,minimum+1):
    count=0
    for j in range(len(no_list)):
        if no_list[j]%i==0:
            count=count+1
    if count==len(no_list):
        gcd=i
print(gcd)
