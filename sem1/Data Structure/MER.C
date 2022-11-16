#include<stdio.h>
#include<conio.h>
main()
{
int i,j,k,a[10],b[10],c[20],m,n;
printf("array 1 size \n");
scanf("%d",&m);
printf("array 2 size \n");
scanf("%d",&n);
printf("array 1 elements in sorted order \n");
for(i=0;i<m;i++)
{
scanf("%d",&a[i]);
}
printf("array 2 elements in sorted order \n");
for(i=0;i<n;i++)
{
scanf("%d",&b[j]);
}
i=0;
j=0;
k=0;
while(i<m&&j<n)
{
printf("\nhlo\n")
if(a[i]<b[j])
c[k++]=a[i++];
else
c[k++]=b[j++];
}
printf("%d\n",c[i]);
getch();
return 0;
}