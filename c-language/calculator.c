//This is my first project in c-language 
//This is simple and basic calculator to perform basic math tasks
//Here is the source code the my project 
//Support me develop this paroject futher and gain valuable knowledge regarding coding in c-language
//I hope you will enjoy this program........👍👍👍👍

#include<stdio.h>
int a,b;
char c;
int main(){
    printf("This is a simple calculator!!!!");
    printf("\nCreated in 'C' language");
    printf("/nCreated by D.varma");
    printf("\nLet's go ..............");
    gather_information();
    Get_operator();
    Condition();
}
void Condition(){
    if(c =='+'){
        printf("\nThen the result is : %d",a+b);
        return_the_function();
    }
    else if(c =='-'){
        printf("\nThen the result is : %d",a-b);
        return_the_function();
    }
    else if(c =='*'){
        printf("\nThen the result is : %d",a*b);
        return_the_function();
    }
    else if(c == '/'){
        printf("\nThen the result is : %d",a/b);
        return_the_function();
    }
    else{
        printf("Please Enter the correct operator....");
        Get_operator();
        Condition();
    }
}
void Get_operator(){
    printf("\nEnter the operator:");
    scanf("%s",&c);
}
void gather_information(){
    printf("\nEnter the first number:");
    scanf("%d",&a);
    printf("Enter the second number:");
    scanf("%d",&b);
    printf("Here are the few operator's to perform the maths ");
    printf("( '+' , '-' , '*' , '/' )");
}
void return_the_function(){
    printf("\n\n*****Use it one more time*****");
    gather_information();
    Get_operator();
    Condition();
}
