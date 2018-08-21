#include<stdio.h>
int main(int argc,char *argv[])  //command line arguments
{
int i;
if(argc!=2)
{exit(1);}
int fact=1;
i=atoi(argv[1]);
for(int j=2;j<=i;j++)
{
    fact=fact*j;
}
printf("%d",fact);
return 0;
}
