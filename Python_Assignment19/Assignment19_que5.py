# write a program which contains filter(), map() and Reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all
# such numbers which are prime. Map will Multiply each number by 2. Reduce will return Maximum from all that numbers.
from functools import reduce

def filterX( elements):
        
    if elements <= 1:
        return False

    for i in range(2, elements):
        if elements % i == 0:
            return False

    return True

def mapX(ret):

    ans = ret * 2
    return ans

def reduceX(no1 , no2):
    
    if no1 > no2:
        return no1
    else:
        return no2

def FMRFunc():
    
    listSize = int(input("Accept number from user : "))
    NumList = []

    for i in range(listSize):

        values = int(input("Enter the numbers in list : "))
        NumList.append(values)

    print("Accepted list is : ", NumList)

    primeNumbers = list(filter(filterX,NumList))
    print("Filter list : ",primeNumbers)

    mapResult = list(map(mapX,primeNumbers))
    print("Map list : ", list(mapResult))

    reduceResult = reduce(reduceX,mapResult)
    print("Reduce Result is : ", reduceResult)

def main():
    FMRFunc()

if(__name__=="__main__"):
    main()
