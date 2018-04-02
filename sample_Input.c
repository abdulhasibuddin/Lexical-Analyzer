#include<stdio.h>
//This is a demo code:
int main()
{
    char str[100];
    int a;

    //This is a single line comment
    gets(str);
    scanf("%d",&a);
    printf("Enter a=%d in the console.",a);

    /*
        This is
        a Multi-line comment.
    */
    printf("Following is a for loop:");
    for(int i=0; ;i++)
    {
        if(str[i]=='\0') { break; }


    }
}
