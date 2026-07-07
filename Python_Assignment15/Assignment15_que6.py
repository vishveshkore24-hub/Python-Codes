# write a lambda function using reduce() which accepts list of numbers and returns the minimum number
from functools import reduce

def Minimum():

    Data = [10,11,13,24,100,20,2,30,40,51,22]
    
    result = reduce(lambda no1, no2  : no1 if no1 <= no2 else no2, Data)

    print("Minimum number of the given list is : ", result)

def main():
    Minimum()

if(__name__=="__main__"):
    main()