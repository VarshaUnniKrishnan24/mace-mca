#include<stdio.h>
int main()
{
int i,j,k,a[10],b[10],c[20],m,n;
printf("enter the size of array 1\n");
scanf("%d",&m);
printf("enter array 1 elements\n");
for(i=0;i<m;i++)
{
scanf("%d",&a[i]);
}
printf("\n enter the size of array 2:\n");
scanf("%d",&n);
printf("\nenter array 2 elements:\n");
for(i=0;i<n;i++)
{
scanf("%d",&b[i]);
}
i=0;j=0;k=0;
while(i<m && j<n)
{
if(a[i]<b[j])
{
c[k]=a[i];
k++;
i++;
}
else
{
c[k]=b[j];
k++;
j++;
}
}
while(i<m)
{
c[k]=a[i];
k++;
i++;
}
while(j<n)
{
c[k]=b[j];
k++;
j++;
}
printf("\n new array after merging :\n");
for(i=0;i<m+n;i++)
{
printf("%d\t",c[i]);
}
getch();
return 0;
}