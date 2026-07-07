# write a lambda function using map() which accepts list of numbers and returns a list of squares of each number

def SquareFun():

    Data = [10,20,30,40]
    squareList = []
    result = list(map(lambda i : i ** i, Data))

    squareList.append(result)
    print("Square List of the given list is : ", result)

def main():
    SquareFun()

if(__name__=="__main__"):
    main()