# write a program which accepts two numbers and prints addition, substraction, multiplication and division
def Addition(no1,no2):
    
    sum = 0 
    sum = no1 + no2
    print("Sum of the two number is : ", sum)

def Substraction(no1,no2):
    
    sub = 0 
    sub = no1 - no2
    print("substraction of the two number is : ", sub)

def Multiplication(no1,no2):
    
    Multi = 0 
    Multi = no1 * no2
    print("Multiplication of the two number is : ", Multi)

def Division(no1,no2):
     
    div = no1 / no2
    print("Division of the two number is : ", div)

def main():
    
    Number1 = int(input("Enter the first Number : "))
    Number2 = int(input("Enter the second Number : "))
    Addition(Number1,Number2)
    Substraction(Number1,Number2)
    Multiplication(Number1,Number2)
    Division(Number1,Number2)

if(__name__=="__main__"):
    main()