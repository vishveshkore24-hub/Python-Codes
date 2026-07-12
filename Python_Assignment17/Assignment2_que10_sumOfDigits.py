#write a program which accepts one number and prints sum of digits

def sumOfDigits(no):

    sum = 0

    for i in str(no):
        sum = sum + int(i)
    print("sum is", sum)
    print(type(str(no)))

def main():
    Number = int(input("Enter Number is : "))
    sumOfDigits(Number)

if(__name__=="__main__"):
    main()