# write a program which contains one lambda function which accepts one parameter return power of two
def powerFunc(no):

    result = lambda value1: value1 ** 2 

    print("Enter the result : ", result(no))

def main():

    Number = int(input("Enter the number is : "))
    powerFunc(Number)

if __name__=="__main__":
    main()