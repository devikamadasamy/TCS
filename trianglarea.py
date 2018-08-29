#n=raw_input()
#a=n.split()
#l=int(a[0])
#b=int(a[1])
import sys
if(len(sys.argv)!=1):
    l=int(sys.argv[1])
    b=int(sys.argv[2])
area=0.5*l*b
area=round(area,2)
print(area)
