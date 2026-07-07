# write a lambda function using filter() which accepts list of numbers and returns a list of odd numbers

def oddList():

    Data = [10,11,13,24,20,30,40,51,22]
    oddNumbers = []
    result = list(filter(lambda i : i % 2 != 0, Data))

    oddNumbers.append(result)
    print("odd numbers List of the given list is : ", result)

def main():
    oddList()

if(__name__=="__main__"):
    main()