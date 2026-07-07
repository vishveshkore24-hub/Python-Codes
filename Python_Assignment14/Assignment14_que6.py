# write a lambda function which accepts one number and returns True if number is even otherwise Even

# Write a lambda function which accepts one number and returns square of that number
def oddEven(no1):

    Num = lambda no1 : True if no1 % 2 == 0 else False 

    print("Check given number is even : ", Num(no1) )

def main():

    Number = int(input("Enter the number : "))

    oddEven(Number)

if(__name__=="__main__"):
    main()