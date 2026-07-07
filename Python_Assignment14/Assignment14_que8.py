# write a lambda function which accepts two numbers and returns addition of that numbers

def Addition(no1,no2):

    Ans = lambda no1,no2 : no1 + no2

    print("Addition of two numbers is : ", Ans(no1,no2) )

def main():

    Number1 = int(input("Enter the number : "))
    Number2 = int(input("Enter the number : "))

    Addition(Number1,Number2)

if(__name__=="__main__"):
    main()