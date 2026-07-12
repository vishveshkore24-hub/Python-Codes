# write a program to accept N numbers from the user and store it into list. Returns addition of all prime numbers from that list. Main
# python file accepts N numbers from users and pass each number to chkPrime() function which is part of our user defined module named as 
# MarvellousNum. Name of the function from main python file should be ListPrime().
import MarvellousNum 

def additionofPrimeNumber():

    listSize = int(input("Enter the list size: "))

    NumList = []

    for i in range(listSize):
        value = int(input("Add number in list: "))
        NumList.append(value)

    print("NumList:", NumList)
    total = 0

    for i in range(listSize):
          if MarvellousNum.CheckPrime(NumList[i]):
              total += NumList[i]
    print("Enter the Addition of Prime Numbers is : ",total) 
    
          
     

def main():

    additionofPrimeNumber()

if __name__ == "__main__":
    main()
