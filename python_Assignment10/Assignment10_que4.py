#write  a program which accepts one number and prints all even numbers till that number
def printEven(no):

    evenNumList = []

    for i in range(no):

        if( i % 2 == 0):
            evenNumList.append(i)
    
    print("Even Numbers are : ", evenNumList)

def main():
    Number = int(input("Enter the Number : "))
    printEven(Number)

if(__name__ == "__main__"):
    main()