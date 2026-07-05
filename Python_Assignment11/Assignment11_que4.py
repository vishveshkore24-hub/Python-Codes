#write a program which accepts one number and print reverse of that number
def ReverseNum(no):

    reverseNum = 0
    for i in str(no):
        i = no % 10
        reverseNum = reverseNum * 10 + i
        no = no // 10
    return reverseNum
    

def main():
    Num = int(input("Enter the Number : "))
    print("Reverse Number is : ",ReverseNum(Num))

if(__name__=="__main__"):
    main()