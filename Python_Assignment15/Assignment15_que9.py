# write lambda function using reduce() which accepts list of numbers and returns the product of all elements
from functools import reduce

def productOP():

    Data = [12, 3, 3, 6, 7, 45,65]
    productList =[]
    result = reduce(lambda no1, no2 : no1 * no2,  Data)

    productList.append(result)

    print("product of all elements is : ", result)

def main():
    productOP()

if(__name__=="__main__"):
    main()

