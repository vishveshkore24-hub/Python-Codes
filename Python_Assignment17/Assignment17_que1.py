import Arithmetic 

def MathOperations(Num1,Num2):

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    selectChoice = int(input("Please select your choice: "))

    if selectChoice == 1:
        Arithmetic.Addition(Num1, Num2)

    elif selectChoice == 2:
        Arithmetic.Substraction(Num1, Num2)

    elif selectChoice == 3:
        Arithmetic.Multiplication(Num1, Num2)

    elif selectChoice == 4:
        Arithmetic.Divison(Num1, Num2)

    else:
        print("Invalid Choice")


def main():
    
    value1 = int(input("Enter the value1 : "))
    value2 = int(input("Enter the value2 : "))
    MathOperations(value1,value2)
    

if(__name__=="__main__"):
    main()