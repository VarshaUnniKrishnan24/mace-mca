#include<stdio.h>
int main()
{
int max,choice,item,front=-1,rear=-1,cqueue[100];
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
 printf("enter the elements\n");
 scanf("\n%d",&item);
  if((front==0 && rear==max-1) || (front==rear+1))
  {
   printf("\n overflow\n");
   break;
  }
  if(front==-1)
  {
  front=0;
  rear=0;
  }
  else
  {
  if(rear==max-1)
  rear=0;
  else
  rear=rear+1;
  }
  cqueue[rear]=item;
  printf("\nvalue inserted");
  break;
}

case 2:
{
 if(front==-1)
 {
  printf("\nunderflow\n");
  break;
  }
 printf("elements deleted from the queue is :%d",cqueue[front]);
  if(front==rear)
   {
    front=-1;
    rear=-1;
    }
    else
    {
    if(front==max-1)
    front=0;
    else
    front=front+1;
    }
    break;
}
case 3:
{
int fpos=front,rpos=rear;
if(front==-1)
{
printf("\nempty queue\n");
break;
}
printf("\nelements in the queue are \n");
if(fpos<=rpos)
while(fpos<=rpos)
{
printf("\n%d",cqueue[fpos]);
fpos++;
}
else
{
while(fpos<=max-1)
{
printf("\n%d",cqueue[fpos]);
fpos++;
}
fpos=0;
while(fpos<=rpos)
{
printf("\n%d",cqueue[fpos]);
fpos++;
}
}
break;
}
case 4:
exit(0);
break;
default:
printf("\n enter valid choice");
}

}
getch();
return 0;
}