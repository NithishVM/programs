#include<stdio.h>
void main()
{
    int n,i,j;
    printf("Generating Pattern for a NUMBER \n");
    printf("Enter a number:\t");
    scanf("%d",&n);
    for(i=1;i<n+1;i++)
    {
        for(j=1;j<=i;j++)
        {
            printf("%d",i);
        }
        printf("\n");
    }
}

/*Nithish V M [RVCE20MCA016] */