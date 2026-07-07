# write a lambda function using reduce() which accepts list of numbers and returns the addition of each elements
from functools import reduce

def additionList():

    Data = [10,11,13,24,20,30,40,51,22]
    
    result = reduce(lambda no1, no2  : no1 + no2  , Data)

    print("Addition List of the given list is : ", result)

def main():
    additionList()

if(__name__=="__main__"):
    main()