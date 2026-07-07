# write a lambda function using filter() which accepts list of numbers and returns a list of even numbers

def evenList():

    Data = [10,11,13,24,20,30,40,51,22]
    evenNumbers = []
    result = list(filter(lambda i : i % 2 == 0, Data))

    evenNumbers.append(result)
    print("even number List of the given list is : ", result)

def main():
    evenList()

if(__name__=="__main__"):
    main()