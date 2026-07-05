# write a program which accepts one number and prints that many numbers in reverse order
def ReverseOrder(no):

    num = []

    for i in range(no,0,-1):
            num.append(i)
    print("Print numbers till the input", num)

def main():
    Number = int(input("Enter the number : "))
    ReverseOrder(Number)

if(__name__=="__main__"):
    main()