#include<stdio.h>
//This is a demo code:
int main()
{
    char str[100];
    int a;

    gets(str);
    scanf("%d",&a);
    printf("Enter a=%d in the console.",a);

    for(int i=0; ;i++)
    {
        if(str[i]=='\0') { break; }


    }
}
