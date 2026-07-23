# write a program which contains one lambda function which accepts two parameter return multiplication of two parameters
def Multiplication(no1,no2):

    result = lambda value1,value2: value1 * value2

    print("Enter the result : ", result(no1,no2))

def main():

    Number1 = int(input("Enter the 1st number is : "))
    Number2 = int(input("Enter the 2nd number is : "))
    Multiplication(Number1,Number2)

if __name__=="__main__":
    main()