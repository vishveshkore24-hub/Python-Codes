# write a lambda function which accepts two numbers and returns maximum number

# Write a lambda function which accepts one number and returns square of that number
def maxNumber(no1,no2):

    MaximumNum = lambda no1,no2 : no1 if no1 > no2 else no2

    print("Maximum number is : ", MaximumNum(no1,no2) )

def main():

    Number1 = int(input("Enter the number : "))
    Number2 = int(input("Enter the number : "))

    maxNumber(Number1,Number2)

if(__name__=="__main__"):
    main()