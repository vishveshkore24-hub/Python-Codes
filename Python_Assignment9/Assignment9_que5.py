def DivOperation(no):
    
    if(no % 3 == 0 and no % 5 == 0):
        print("The given number is divisible by 3 and 5")
    else:
        print("Given Number is not divisible by 3 & 5")

def main():
    
    Number = int(input("enter the Number is : "))

    DivOperation(Number)

if(__name__ == "__main__"):
    main()