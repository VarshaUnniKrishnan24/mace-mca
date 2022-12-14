#include<stdio.h>
#include<stdlib.h>
void create();
void display();
void insert_begin();
void insert_end();
void insert_pos();
void delete_begin();
void delete_end();
void delete_pos();

struct node
{
int info;
struct node*next;
};
struct node*start=NULL;

int main()
{
int choice;
printf("\nMENU\n1.create\n2.display\n3.insert at the beginning\n 4.insert at the end\n\n5.insert at specified position\n\n6.delete from beginning\n7.delete from the end\n8.delete from the specified position\n9.exit\n");
while(1){
printf("enter your choice:");
scanf("%d",&choice);
switch(choice)
{
case 1:
create();
break;
case 2:
display();
break;
case 3:
insert_begin();
break ;
case 4:
insert_end();
break;
case 5:
insert_pos();
break;
case 6:
delete_begin();
break;
case 7:
delete_end();
break;
case 8:
delete_pos();
break;
case 9:
exit(0);
break;
default:
printf("\nwrong choice");
break;
}
}
return 0;
}


void create()
{
struct node*temp,*ptr;
temp=(struct node*)malloc(sizeof(struct node));
if(temp==NULL)
{
printf("\n out of memory space\n");
exit(0);
}
printf("enter the data value for the node:");
scanf("%d",&temp->info);
temp->next=NULL;
if(start==NULL)
{
start=temp;
}
else
{
ptr=start;
while(ptr->next!=NULL)
{
ptr=ptr->next;
}
ptr->next=temp;
}
}

void display()
{
struct node*ptr;
if(start==NULL)
{
printf("\n list is empty");
}
else
{
ptr=start;
printf("the list elements are:\n");
while(ptr!=NULL)
{
printf("%d",ptr->info);
ptr=ptr->next;
}
}
}

void insert_begin()
{
struct node*temp;
temp=(struct node*)malloc(sizeof(struct node));
if(temp==NULL)
{
printf("out of memory space:");
return;
}
printf("\n enter the data value for the node:");
scanf("%d",&temp->info);
temp->next=NULL;
if(start==NULL)
{
start=temp;
}
else
{
temp->next=start;
start=temp;
}
}

void insert_end()
{
struct node*temp,*ptr;
temp=(struct node*)malloc(sizeof(struct node));
if(temp==NULL)
{
printf("\n out of memory space");
return;
}
printf("\n enter the data value for the node:");
scanf("%d",&temp->info);
temp->next=NULL;
if(start==NULL)
{
start=temp;
}
else
{
ptr=start;
while(ptr->next!=NULL)
{
ptr=ptr->next;
}
ptr->next=temp;
}
}

void insert_pos()
{
struct node*ptr,*temp;
int i,pos;
temp=(struct node*)malloc(sizeof(struct node));
if(temp==NULL)
{
printf("\nout of memory space");
return;
}
printf("\n enter the position for new node to be inserted:");
scanf("%d",&pos);
printf("\n enter the data value of the node:");
scanf("%d",&temp->info);

temp->next=NULL;
if(pos==0)
{
temp->next=start;
start=temp;
}
else
