# Write a program which contains filter(), map(), reduce() in it. Python application which contains one list numbers. List contains the
# numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal
#  to 90. Map function will increase each number by 10. Reduce will return product of that all numbers
from functools import reduce

def filterX( elements):
        
    if( 70 <= elements <= 90):
      return elements

def mapX(ret):

    ret += 10
    return ret

def reduceX(no1 , no2):
    
    return no1 * no2

def FMRFunc():
    
    listSize = int(input("Accept number from user : "))
    NumList = []

    for i in range(listSize):

        values = int(input("Enter the numbers in list : "))
        NumList.append(values)

    print("Accepted list is : ", NumList)

    Fresult = list(filter(filterX,NumList))
    print("Filter list : ",Fresult)

    increaseResult = list(map(mapX,Fresult))
    print("Map list : ", list(increaseResult))

    productResult = reduce(reduceX,increaseResult)
    print("Reduce Result is : ", productResult)

def main():
    FMRFunc()

if(__name__=="__main__"):
    main()