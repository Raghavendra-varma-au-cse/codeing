#This is the advance calculator used for windows,linux,macos in command line.
#First,U need download and install python.
#Second,Copy the code or download the calculator_final.py file and run 💥💥💥.
#I hope u will enjoy the project
#In future i will update the code and make it more advance.
#THANK YOU........🙏🙏🙏🙏

#bin/usr/env python3
def Gather_information():
    global num1,num2
    num1 = int(input("\nEnter the first number :"))
    num2 = int(input("\nEnter the second number :"))
    print("Here are the few operator to perform math\n\t'+'\tAddition\n\t'-'\tSubraction\n\t'*'\tMultiplation")
    print("\t'/'\tDivision\n\t'//'\tQuotion\n\t'%'\tRemainder\n\t'**'\tFirst number whole power second number")
def Get_operator():
    global operator
    operator = input("\nEnter the operator you needed :")
def conditon():
    if operator == '+':
        print(f"\nThe answer is : {num1+num2}")
        return_the_function()
    elif operator == '-':
        print(f"\nThe answer is : {num1-num2}")
        return_the_function()
    elif operator == '*':
        print(f"\nThe answer is : {num1*num2}")
        return_the_function()
    elif operator == '/':
        print(f"\nThe answer is : {num1/num2}")
        return_the_function()
    elif operator == '**':
        print(f"\nThe answer is : {num1**num2}")
        return_the_function()
    elif operator == '//':
        print(f"\nThe quotion is : {num1//num2}")
        return_the_function()
    elif operator == '%':
        print(f"\nThe remainder is : {num1%num2}")
        return_the_function()
    else:
        print("\nPlease Enter correct operator.....")
        print("Here are the few operator to perform math\n\t'+'\tAddition\n\t'-'\tSubraction\n\t'*'\tMultiplation")
        print("\t'/'\tDivision\n\t'//'\tQuotion\n\t'%'\tRemainder\n\t'**'\tFirst number whole power second number")
        Get_operator()
        conditon()
def return_the_function():
    print("\n------------------------------")
    print("\n\n***Use it one more time***")
    Gather_information()
    Get_operator()
    conditon()
print("-----------------------------------")
print("\n\n===========  Calculator ============")
print("========= Created in python ===========")
print("============= By D.Varma ==============")
Gather_information()
Get_operator()
conditon()
