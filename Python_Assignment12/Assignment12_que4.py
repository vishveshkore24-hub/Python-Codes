# write a program which accepts one number and prints that many numbers starting from 1
def printNumbers(no):
    num = []
    for i in range(no+1):
        if( i != 0):
            num.append(i)
    print("Print numbers till the input", num)

def main():
    Number = int(input("Enter the number : "))
    printNumbers(Number)

if(__name__=="__main__"):
    main()