# write a lambda function which accepts two numbers and returns minimum number

# Write a lambda function which accepts one number and returns square of that number
def minNumber(no1,no2):

    MinimumNum = lambda no1,no2 : no1 if no1 < no2 else no2

    print("Minimum number is : ", MinimumNum(no1,no2) )

def main():

    Number1 = int(input("Enter the number : "))
    Number2 = int(input("Enter the number : "))

    minNumber(Number1,Number2)

if(__name__=="__main__"):
    main()