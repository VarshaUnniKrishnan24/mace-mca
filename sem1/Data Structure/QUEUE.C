#include<stdio.h>
int main()
{
int max,choice,front=-1,rear=-1,queue[100];
printf("\n enter the size of queue:");
scanf("%d",&max);
printf("\n queue operations");
printf("\n1.insert\n2.delete\n3.display\n4.exit");
while(choice!=4)
{
printf("\nenter your choice:");
scanf("%d",&choice);
switch(choice)
{
 case 1:
 {
 int item;
 printf("enter the elements\n");
 scanf("\n%d",&item);
  if(rear==max-1)
  {
   printf("\n overflow\n");
   break;
  }
  if(front==-1 && rear==-1)
  {
  front=0;
  rear=0;
  }
  else
  {
  rear=rear+1;
  }
  queue[rear]=item;
  printf("\nvalue inserted");
  break;
}
case 2:
{
 int item;
 if(front==-1||front>rear)
 {
  printf("\nunderflow\n");
  }
 else
 {
  item=queue[front];
  if(front==rear)
   {
    front=-1;
    rear=-1;
    }
    else
    {
    front=front+1;
    }    }
    printf("\nvalue deleted is %d",item);
    break;
}
case 3:
{int i;
if(rear==-1)
printf("\nempty queue\n");
else
{
printf("\nelements in the queue are \n");
for(i=front;i<=rear;i++)
{printf("\n%d",queue[i]);}
break;
}
case 4:
exit(0);
break;
default:
printf("\n enter valid choice");
}

}
}
getch();
return 0;
}