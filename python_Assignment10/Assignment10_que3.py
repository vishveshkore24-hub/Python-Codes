# Write a program which accepts one number and prints factorial of that number
def Factorial(no):

    fact = 1 
    for i in range(1, no + 1):
        fact *= i 
    
    print("factorial numbers are : ", fact)

def main():
    Number = int(input("Enter the Number is : "))

    Factorial(Number)

if(__name__ == "__main__"):
    main()