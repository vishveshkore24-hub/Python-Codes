# Write a program which accepts one number and prints sum of all factorial number
def Factorial(no):
    
    sum =0
    for i in range(1, no):
        if(no % i == 0 ):
            sum += i
    print ("Sum of factorial numbers is : ", sum)

def main():
    Number = int(input("Enter the Number is : "))

    Factorial(Number)

if(__name__ == "__main__"):
    main()