#import sys
#if(len(sys.argv)!=1):
 #   dia=int(sys.argv[1])
dia=int(raw_input())   
rad=dia/2.0
area=(22/7.0)*rad*rad
area=round(area,2)
print(area)
