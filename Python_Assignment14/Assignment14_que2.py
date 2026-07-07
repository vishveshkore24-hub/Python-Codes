# Write a lambda function which accepts one number and returns square of that number
def Qube(no):

    cube = lambda no : no * no * no

    print("Square of the given number is : ", cube(no) )

def main():

    Number = int(input("Enter the number : "))

    Qube(Number)

if(__name__=="__main__"):
    main()