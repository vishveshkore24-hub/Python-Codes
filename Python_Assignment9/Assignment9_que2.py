def ChkGreater(no1,no2):

    if(no1 > no2):
        print("Print greater Number is : " , no1)
    elif(no2 > no1):
        print("Print greater number is : ", no2)
    else:
        print("Both are qual")

def main():
    
    num1 = int(input("Enter first Number is : "))
    num2 = int(input("Enter second number is : "))

    ChkGreater(num1,num2)

if(__name__ == "__main__"):
    main()