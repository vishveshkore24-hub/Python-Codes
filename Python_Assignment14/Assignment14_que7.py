# write a lambda function which accepts one number and returns True if number is divisible by 5

def modFive(no1):

    Num = lambda no1 : True if no1 % 5 == 0 else False 

    print("Check given number is divisible by 5 : ", Num(no1) )

def main():

    Number = int(input("Enter the number : "))

    modFive(Number)

if(__name__=="__main__"):
    main()