#include<stdio.h>
int main()
{
int stack[100],choice,n,top,x,i;
top=-1;
printf("enter the size of stack");
scanf("%d",&n);
printf("\nstack operations using array");
printf("\n1.push\n2.pop\n3.display\n4.exit");
do
{
printf("\nenter the choice:");
scanf("%d",&choice);
switch(choice)
{
case 1:
{
    if(top>=n-1)
    printf("\n stack is overflow");
    else
    {
    printf("enter the value to be pushed:");
    scanf("%d",&x);
    top++;
    stack[top]=x;
    }
    break;
}
case 2:
{
   if(top<=-1)
   printf("\nstack is underflow");
   else
   {
   printf("\n the popped element is %d",stack[top]);
   top--;
   }
   break;
   }
case 3:
   {
     if(top>=0)
     {
     printf("\n the elements in stack\n");
     for(i=top;i>=0;i--)
     {
     printf("\n%d",stack[i]);
     }
     }
     else
     printf("\nstack is empty");
     break;
   }
case 4:
  {
     printf("\n existing...");
     break;
  }
default:
{
printf("\n please enter valid choice(1/2/3/4");
}
}
   }while(choice!=4);
   getch();
   return 0;
   }