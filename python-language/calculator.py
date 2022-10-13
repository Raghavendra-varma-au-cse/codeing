#This is my first project in python-language 🥇🥇🥇
#This is simple and basic calculator to perform basic math tasks
#Here is the source code the my project 
#Support me develop this paroject futher and gain valuable knowledge regarding coding in python-language
#I hope you will enjoy this program........👍👍👍👍


#bin/usr/env python3
num1 = int(input("Enter the fitst number : "))
num2 = int(input("Enter the second number : "))
reponse = str(input("To know about the operators type 'y/n' :"))
if reponse =='y':
    print("Here are the few operators to perform the math task!")
    print(" '+' = Addition\n '-' = subraction\n '/' = division \n '*' = multipluction\n '**' = expontental")
    operator = input("Enter the operator :")
elif reponse=='n':
    operator = input("Enter the operator :")
else:
    print("Please enter correct input.....")
if operator=='+':
    print("The answer is : ",num1+num2)
elif operator=='-':
    print("The answer is : ",num1-num2)
elif operator=='*':
    print("The answer is : ",num1*num2)
elif operator =='/':
    print("The answer is :",num1/num2)
elif operator == '**':
    print("The answer is : ",num1**num2)
else:
    print("Please Enter correct operator.....")
exit()
