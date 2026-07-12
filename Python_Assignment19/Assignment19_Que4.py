# write a program which contains filter(), map() and Reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all
# such numbers which are EVEN. Map will calculate its square. Reduce will return addition of all that numbers.
from functools import reduce

def filterX( elements):
        
    if( elements % 2 == 0):
      return elements

def mapX(ret):

    ret ** 2
    return ret

def reduceX(no1 , no2):
    
    return no1 + no2

def FMRFunc():
    
    listSize = int(input("Accept number from user : "))
    NumList = []

    for i in range(listSize):

        values = int(input("Enter the numbers in list : "))
        NumList.append(values)

    print("Accepted list is : ", NumList)

    evenNumber = list(filter(filterX,NumList))
    print("Filter list : ",evenNumber)

    evenSquare = list(map(mapX,evenNumber))
    print("Map list : ", list(evenSquare))

    evenSum = reduce(reduceX,evenSquare)
    print("Reduce Result is : ", evenSum)

def main():
    FMRFunc()

if(__name__=="__main__"):
    main()
