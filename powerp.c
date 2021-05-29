#include<stdio.h>
void main()
{
    while(1)
    {
    int x,n,z=1;
    printf("\n\nEnter the value of X:\t");
    scanf("%d",&x);
    printf("Enter the value of N:\t");
    scanf("%d",&n);
    while(n>0)
    {
        z=x*z;
        --n;
    }
    printf("The Value of X^n is %d",z);
    }
}

/*Nithish V M [RVCE20MCA016] */