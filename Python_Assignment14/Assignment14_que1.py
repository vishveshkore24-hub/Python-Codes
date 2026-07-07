# Write a lambda function which accepts one number and returns square of that number
def Square(no):

    square = lambda no : no * no

    print("Square of the given number is : ", square(no) )

def main():

    Number = int(input("Enter the number : "))

    Square(Number)

if(__name__=="__main__"):
    main()