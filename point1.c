#include<stdio.h>
void main()
{
    int x,y;
    int *ptr;
    x=10;
    ptr= &x;
    y = *ptr;
    printf("%d is stored in location %u\n",x,&x);
    printf("%d is stored in location %u\n",*&x,*&ptr);
}