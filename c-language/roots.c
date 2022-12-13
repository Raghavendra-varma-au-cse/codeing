#include<stdio.h>
#include<math.h>
int main(){
    int x,a,b,c,D,X,Y;
    printf("To Calculate the roots of the given quadratic equation\n\n");
    printf("Please Enter a b c values: ");
    scanf("%d %d %d", &a, &b, &c);
    if(a != 0){
        if(b<0){
            printf("\n\nThe quadratic equation is %dx^2 - %dx + %d = 0\n\n",a,abs(b),c);
        }
        else if(c<0){
            printf("\n\nThe quadratic equation is %dx^2 + %dx - %d = 0\n\n",a,b,abs(c));
        }
        else{
            printf("\n\nThe quadratic equation is %dx^2 - %dx + %d = 0\n\n",a,abs(b),c);
        }
        D = b*b - 4*a*c;
        if(D > 0){
            printf("This equation has real and distinct roots (Unreal)\n\n");
            X = (-b+sqrt(b*b - 4*a*c))/2*a;
            Y = (-b-sqrt(b*b - 4*a*c))/2*a;
            printf("Roots are (%d,%d)", X, Y);
        }
        else if(D < 0){
            printf("This equation has imaginary and unreal roots\n\n");
            X = -b/2*a;
            Y = sqrt(abs(b*b - 4*a*c))/2*a;
            printf("Roots are (%d + i%d) and (%d - i%d)", X, Y, X, Y);
        }
        else{
            printf("This equation has real and equal roots\n\n");
            X = (-b+sqrt(b*b - 4*a*c))/2*a;
            Y = (-b-sqrt(b*b - 4*a*c))/2*a;
            printf("Roots are (%d,%d)", X, Y);
        }
        printf("\n\n");

    }
    else{
        printf("Equation is Invalid (a != 0)");
    }
    return 0;
}
