#include<stdio.h>
void main()
{
    while(1){
    int lvl,ca,ea,gross,Net,basic_pay,perks;
    char name[100];
    printf("\nEnter the Employee details below:\n");
    printf("Enter the Employee Name:\t");
    scanf("%s",name);
    printf("Enter the Employee Level:\t");
    scanf("%d",&lvl);
    printf("Enter the Basic pay of the employee:\t");
    scanf("%d",&basic_pay);
    if(lvl==1)
    {
        perks = 1500;
        gross=(basic_pay+(basic_pay*0.25)+perks);
    }
    else if(lvl==2)
    {
        perks =950;
        gross=(basic_pay+(basic_pay*0.25)+perks);
    }
    else if(lvl==3)
    {
        perks =600;
        gross=(basic_pay+(basic_pay*0.25)+perks);
    }
    else if(lvl==4)
    {
        perks=250;
        gross=(basic_pay+(basic_pay*0.25)+perks);
    }
    else
    {
        printf("Enter a Valid Level");
    }
    if(gross<=2000 && gross != 0)
    {
        printf("The Net Salary is:\t");
        printf(" %d ",gross);
    }
    else if(gross>2000 && gross<=4000)
    {
        printf("The Net Salary is:\t");
        int v=(gross-gross*0.03);
        printf(" %d ",v);
    }
    else if(gross>4000 && gross <=5000)
    {
        printf("The Net Salary is:\t");
        int v=(gross-gross*0.05);
        printf(" %d ",v);
    }
    else if(gross>5000)
    {
        printf("The Net Salary is:\t");
        int v=(gross-gross*0.03);
        printf(" %d ",v);
    }
    }
}

/*Nithish V M [RVCE20MCA016] */