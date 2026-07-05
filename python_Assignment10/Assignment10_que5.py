#write  a program which accepts one number and prints all odd numbers till that number
def printOdd(no):

    oddNumList = []

    for i in range(no):

        if( i % 2 != 0):
            oddNumList.append(i)
    
    print("Even Numbers are : ", oddNumList)

def main():
    Number = int(input("Enter the Number : "))
    printOdd(Number)

if(__name__ == "__main__"):
    main()