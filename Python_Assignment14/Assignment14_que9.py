# write a lambda function which accepts two numbers and returns Multiplication of that numbers

def Multiplication(no1,no2):

    Ans = lambda no1,no2 : no1 * no2

    print("Multiplication of two numbers is : ", Ans(no1,no2) )

def main():

    Number1 = int(input("Enter the number : "))
    Number2 = int(input("Enter the number : "))

    Multiplication(Number1,Number2)

if(__name__=="__main__"):
    main()